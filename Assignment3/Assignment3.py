#!/usr/bin/env python3


def get_slice(content: str, piece: str):
    start, stop = piece[1:-1].split(":")
    start = int(start) if start else 0
    stop = int(stop) if stop else 0
    if stop != 0:
        return content[start:stop]
    else:
        return content[start:]


def read_file(path: str) -> str:
    content = []
    with open(path, 'r') as f:
        content = f.readlines()
    return "\n".join(content)


def decode_1st_line(content: str) -> str:
    return content[::2] + content[1::2]


def decode_2nd_line(content: str, slices: str) -> str:
    result = ""
    for piece in slices.split(", "):
        tmp = get_slice(content, piece)
        print(f"Found fragment {tmp}")
        result += tmp
    return result


def main():
    content = read_file("assignment3_1.txt")
    slices = decode_1st_line(content.splitlines()[0])
    print(f"Found slices: {slices}")
    result = decode_2nd_line(content.splitlines()[2], slices)
    print(result)


if __name__ == "__main__":
    main()
