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
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        self.encoding = sys.stdin.encoding

#    def run(self, command: str) -> str:
#        print("Writing to stdin...")
#        self.shell.stdin.write(command.encode(self.encoding))
#        print("Written\nWaiting for output...")
#        self.shell.wait(5)
#        print("Received\nDecoding...")
#        result = self.shell.stdout.readline().decode(self.encoding)
#        errors = self.shell.stderr.readline().decode(self.encoding)
#        return result


def main():
    print("Creating shell...")
    # sh = Shell()
    print("Created")

    print("Running 'dir'")
    res = subprocess.run(["dir"], capture_output=True, text=True, shell=True).stdout
    print(res)
    res = subprocess.run(["cd .."], capture_output=True, text=True, shell=True).stdout
    print(res)
    res = subprocess.run(["dir"], capture_output=True, text=True, shell=True).stdout
    print(res)
    pass


if __name__ == "__main__":
    main()
