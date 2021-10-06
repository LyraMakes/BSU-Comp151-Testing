#!/usr/bin/env python3
import dataclasses
import datetime
import os
import shlex

import glob


def _draw_pb(percent, length=20):
    print(
        f"\r[{''.join(['=' if i < int(length * percent) else ' ' for i in range(length)])}] {(percent * 100):.2f}%",
        end=""
    )


class FilePermissions:
    isDir: bool
    isSym: bool
    isExe: bool
    owner_read: bool
    owner_write: bool
    owner_read: bool
    owner_read: bool
    owner_write: bool
    owner_read: bool
    owner_read: bool
    owner_write: bool
    owner_read: bool


@dataclasses.dataclass(order=True)
class FileStats:
    perms: str
    hlinks: int
    owner: str
    group: str
    size: int
    modified: datetime.datetime
    name: str


class ProgressBar:
    TERMINAL_WIDTH = os.get_terminal_size().columns - 12

    def __init__(self, length):
        self.length = length

    def update(self, percent):
        _draw_pb(percent, self.length)


# noinspection PyArgumentList,PyMethodMayBeStatic
class Shell:
    def __init__(self):
        self.__BUILTINS = {
            "echo": self.__bash_echo,
            "ls": self.__bash_ls
        }
        self.pwd = os.getcwd()
        self.shell = "bash"
        self.dirhist = []

    def run(self, command: str) -> str:
        cmd = shlex.split(command)
        if cmd[0] in self.__BUILTINS:
            return self.__BUILTINS[cmd[0]](cmd[1:])

    def __bash_echo(self, *args) -> str:
        return " ".join(args[0])

    def __get_properties(self, file):
        stats = os.stat(file, follow_symlinks=False)
        date = datetime.datetime.fromtimestamp(stats.st_mtime, tz=datetime.timezone.utc)
        print(date.strftime('%Y-%m-%d-%H:%M'))
        fStats = FileStats("", 0, "", "", stats.st_size, date, os.path.basename(file))
        return fStats

    def __bash_ls(self, *args) -> str:
        path = args[0][0]

        dir_path = os.path.join(self.pwd, path)
        dir_path = os.path.join(dir_path, "*")
        print(dir_path)
        raw = [os.path.abspath(x) for x in glob.glob(dir_path)]

        processed = [self.__get_properties(x) for x in raw]

        print(raw)
        print(processed[0])

        return "EGUH"




def main():
    sh = Shell()
    res = sh.run("ls ..")
    print(res)


if __name__ == "__main__":
    main()
