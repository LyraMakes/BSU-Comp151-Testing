#!/usr/bin/env python3
from typing import List


def batch_convert_unames(content, is_file=True, output_file="") -> List[str]:
    if is_file:
        with open("names.txt", 'r') as infile:
            names = [x.strip() for x in infile.readlines()]
    else:
        names = content

    usernames = []
    for name in names:
        first, last = name.split(' ')
        usernames.append(f"{first[0]}{last[:7]}\n")

    if len(output_file) > 0:
        with open(output_file, 'w') as outfile:
            outfile.writelines(usernames)
    return [x.strip() for x in usernames]


def ConvertNames():
    unames = batch_convert_unames("names.txt", is_file=True, output_file="usernames.txt")
    print(unames)


def main():
    ConvertNames()


if __name__ == "__main__":
    main()
