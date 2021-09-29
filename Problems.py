def chapter_five_problem_1():
    """Prints out the first 3 odd indexed characters"""
    user_input = input("Enter a string: ")
    if len(user_input) < 6:
        raise ValueError("String is not long enough")
    print(user_input[1:6:2])


def chapter_five_problem_2():
    """Takes first 2 characters and appends"""
    user_input = input("Enter a string: ")
    if len(user_input) < 2:
        raise ValueError("String is not long enough")
    print(user_input + user_input[:2])


def chapter_five_problem_3():
    """Takes last 3 characters and prepends twice"""
    user_input = input("Enter a string: ")
    if len(user_input) < 2:
        raise ValueError("String is not long enough")
    print((user_input[-3:] * 2) + user_input)


def main():
    chapter_five_problem_3()


if __name__ == "__main__":
    main()
