#!/usr/bin/env python3

def __show_help(*args):
    """Shows the help screen"""
    bins = [(key, value.__doc__) for (key, value) in builtins.items()]
    dirs = [(f"-!{key}", value.__doc__) for (key, value) in directives.items()]

    colsize = max([len(key) for (key, value) in dirs + bins])
    print("Directives available:")
    for name, doc in dirs:
        print(f"  {name:>{colsize}}    {doc}")

    print("Commands available:")
    for name, doc in bins:
        print(f"  {name:>{colsize}}    {doc}")


def __list_files(*args):
    """Lists currently available scripts"""
    import os
    res = os.walk(".")

    file_list = []

    for stem, dirs, files in res:
        if any([x in stem for x in ignore_dirs]):
            continue

        file_list.extend([f"{stem}\\{file}"[2:-3] for file in files if file.endswith(".py")])

    for file in file_list:
        print(file)


builtins = {
    'ls': __list_files
}

directives = {
    'help': __show_help
}

ignore_dirs = [
    "venv",
    ".git",
    ".idea",
    "__pycache__"
]


def main():


    print("Welcome to Lyra's BSU Comp151 Repository.")
    print("Please type `-!help` for help")

    while True:
        usr_inp = input(">>>")

        if usr_inp.startswith('-!'):
            usr_inp = usr_inp[2:]
            if usr_inp in directives:
                directives[usr_inp]()
            elif usr_inp in ["exit", "quit", "break", "stop"]:
                break
            else:
                print(f'Directive: `{usr_inp}` unrecognised')
        elif usr_inp in builtins:
            builtins[usr_inp]()
        else:
            print(f'Command: `{usr_inp}` unrecognised')
    print("Exiting...")


if __name__ == "__main__":
    main()
