#!/usr/bin/env python3
import os
import shlex

import glob


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

    def __bash_ls(self, *args) -> str:
        path = args[0][0]

        dir_path = os.path.join(self.pwd, path)
        dir_path = os.path.join(dir_path, "*")
        print(dir_path)
        raw = glob.glob(dir_path)

        print(raw)

        return "EGUH"




def main():
    sh = Shell()
    res = sh.run("ls ..")
    print(res)


if __name__ == "__main__":
    main()
