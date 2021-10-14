#!/usr/bin/env python3
import dataclasses
import datetime
import math
import os
import shlex
import pathlib
import glob
import stat
import getpass
import platform

# #def _draw_pb(percent, length=20):
#    print(
#        f"\r[{''.join(['=' if i < int(length * percent) else ' ' for i in range(length)])}] {(percent * 100):.2f}%",
#        end=""
#    )
from typing import List


class FilePermissions:
    def __init__(self, mode, path):
        self.owner_read = mode & stat.S_IRUSR
        self.owner_write = mode & stat.S_IWUSR
        self.owner_execute = mode & stat.S_IXUSR

        self.group_read = mode & stat.S_IRGRP
        self.group_write = mode & stat.S_IWGRP
        self.group_execute = mode & stat.S_IXGRP

        self.other_read = mode & stat.S_IROTH
        self.other_write = mode & stat.S_IWOTH
        self.other_execute = mode & stat.S_IXOTH

        self.isExe = self.owner_execute or self.group_execute or self.other_execute
        self.isDir = os.path.isdir(path)
        self.isSym = os.path.islink(path)

    def __str__(self):
        res = "l" if self.isSym else "d" if self.isDir else "-"
        res += "r" if self.owner_read else "-"
        res += "w" if self.owner_write else "-"
        res += "x" if self.owner_execute else "-"
        res += "r" if self.group_read else "-"
        res += "w" if self.group_write else "-"
        res += "x" if self.group_execute else "-"
        res += "r" if self.other_read else "-"
        res += "w" if self.other_write else "-"
        res += "x" if self.other_execute else "-"
        return res

    def __repr__(self):
        return self.__str__()


@dataclasses.dataclass(order=True)
class FileStats:
    perms: FilePermissions
    hlinks: int
    owner: str
    group: str
    size: int
    modified: datetime.datetime
    name: str


# #class ProgressBar:
#    TERMINAL_WIDTH = os.get_terminal_size().columns - 12
#
#    def __init__(self, length):
#        self.length = length
#
#    def update(self, percent):
#        _draw_pb(percent, self.length)


# noinspection PyArgumentList,PyMethodMayBeStatic
class Shell:
    def __init__(self):
        self.__BUILTINS = {
            "echo": self.__bash_echo,
            "ls": self.__bash_ls,
            "clear": self.__bash_clear
        }
        self.user = ""
        self.pwd = os.getcwd()
        self.shell = "bash"
        self.dirhist = []
        self.env = []
        self.color_enabled = False
        self.user = getpass.getuser()
        self.host = platform.node()
        self.ps1 = f"┌──({self.user}@{self.host})-[{self.pwd}]\n└─$"

    # noinspection PyUnreachableCode
    def run(self, command: str) -> str:
        cmd = shlex.split(command)
        if cmd[0] in self.__BUILTINS:
            return self.__BUILTINS[cmd[0]](cmd[1:])
        elif False:
            pass
        else:
            print(f"-bash: {cmd[0]}: command not found")

    def __get_owner(self, path: pathlib.Path):
        try:
            return path.owner()
        except NotImplementedError:
            return "win32-unk"

    def __get_properties(self, file) -> FileStats:
        stats = os.stat(file, follow_symlinks=False)
        date = datetime.datetime.fromtimestamp(stats.st_mtime, tz=datetime.timezone.utc)
        perms = FilePermissions(stats.st_mode, file)
        path = pathlib.Path(file)
        fStats = FileStats(perms, stats.st_nlink,
                           self.__get_owner(path), self.__get_group(path),
                           stats.st_size, date, os.path.basename(file))
        return fStats

    def __get_group(self, path: pathlib.Path):
        try:
            return path.group()
        except NotImplementedError:
            return "win32-unk"

    def __bash_echo(self, *args) -> str:
        res = " ".join(args[0])
        print(res)
        return res

    def __bash_ls(self, *args) -> List[FileStats]:
        def nlen(num: int) -> int:
            return int(math.log10(num) + 1) if num else 1

        def upad(dt: datetime.datetime, form: str) -> str:
            return str(int(dt.strftime(form)))

        def pad(content, padding: int) -> str:
            return f"{content:>{padding}}"

        path = args[0][0] if args[0] else "."

        dir_path = os.path.join(self.pwd, path)
        dir_path = os.path.join(dir_path, "*")

        raw = [os.path.abspath(x) for x in glob.glob(dir_path)]

        if not raw:
            return []

        processed = [self.__get_properties(x) for x in raw]

        c2_s = max([nlen(x.hlinks) for x in processed])
        c3_s = max([len(x.owner) for x in processed])
        c4_s = max([len(x.group) for x in processed])
        c5_s = max([nlen(x.size) for x in processed])
        c7_s = max([len(upad(x.modified, "%d")) for x in processed])

        for file in processed:
            line = f"{file.perms} {pad(file.hlinks, c2_s)} " \
                   f"{pad(file.owner, c3_s)} {pad(file.group, c4_s)} {pad(file.size, c5_s)} " \
                   f"{file.modified.strftime('%b')} {pad(upad(file.modified, '%d'), c7_s)} " \
                   f"{file.modified.strftime('%H:%M')} {file.name}"
            print(line)

        return processed

    def __bash_clear(self, *args):
        os.system("cls" if 'nt' in os.name else 'clear')


def main():
    sh = Shell()
    while True:
        usr_inp = input(f"{sh.ps1} ")
        if usr_inp in ["quit", "break", "exit"]:
            break
        res = sh.run(usr_inp)
    print(sh.user, sh.host)


if __name__ == "__main__":
    main()
