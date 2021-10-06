#!/usr/bin/env python3
def main():
    with open("exercise3.txt") as f:
        [print(x.strip().upper()) for x in f.readlines()]


if __name__ == "__main__":
    main()
