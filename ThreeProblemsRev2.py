#!/usr/bin/env python3
from typing import Callable
import datetime


def safe_eval(content: str):
    return eval(content, {'__builtins__': None}, {})


def check_age(age: int, *args) -> bool:
    return age >= 0


def true(*args) -> bool:
    return True


def input_int(message: str, constraint: Callable):
    if not constraint:
        constraint = true
    while True:
        user_input = input(message)
        try:
            user_input = int(user_input)
            if not constraint(user_input):
                raise ValueError
            else:
                return user_input
        except ValueError:
            print("Value entered was invalid")


def problem1():
    name = input("Please enter your name: ")
    age = input_int("Please enter your age: ", check_age)
    date = datetime.date.today().year
    print(f"Hello {name}, you were born in {date - age}.")


def problem2():
    end = input_int("Ending value: ")
    total = 0
    for i in range(2, end + 1):
        total += i
    print(f"The sum from 2 to {end} is {total}")


def problem3():
    print("Simple Python Calculator using a sanitized eval")
    end_words = ["break", "quit", "end", "stop", "exit"]
    user_input = input(">>> ")
    while user_input not in end_words:
        try:
            print(safe_eval(user_input))
        except(TypeError, SyntaxError):
            print("Incorrectly formatted expression")
        user_input = input(">>> ")
    print("Exiting...")


def main():
    problem1()
    print("\n\n---------------------------\n\n")
    problem2()
    print("\n\n---------------------------\n\n")
    problem3()


if __name__ == "__main__":
    main()
