#!/usr/bin/env python3


def run(command: str) -> (str, str):
    import subprocess
    import sys
    import shlex
    out_encoding = sys.stdout.encoding
    err_encoding = sys.stderr.encoding

    tokens = shlex.split(command)

    proc = subprocess.Popen(tokens, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out_text = out.decode(out_encoding) if out else ""
    err_text = err.decode(err_encoding) if err else ""

    return out_text, err_text


def main():
    while True:
        (out, err) = run(input(">>> "))
        print(out)
        print(err)


if __name__ == "__main__":
    main()
