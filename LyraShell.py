import subprocess
import sys
import os


def clear_screen():
    os.system("clear" if 'linux' in sys.platform else "cls")


def is_linux() -> bool:
    return 'linux' in sys.platform


class Shell:
    def __init__(self):
        self.shell = subprocess.Popen(
            ['sh' if is_linux() else 'cmd.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        self.encoding = sys.stdin.encoding

    def run(self, command: str) -> str:
        self.shell.stdin.write(command.encode(self.encoding))
        result = self.shell.stdout.readline().decode(self.encoding)
        errors = self.shell.stderr.readline().decode(self.encoding)
        return result
