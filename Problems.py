def chapter_five_problem_1():
    """Prints out the first 3 odd indexed characters"""
    user_input = input("Enter a string: ")
    if len(user_input) < 6:
        raise ValueError("String is not long enough")
    print(user_input[1:6:2])


def main():
    chapter_five_problem_1()


if __name__ == "__main__":
    main()
