#!/usr/bin/python3
"""defines a function read_file(filename="")"""


def read_file(filename="UTF8"):
    """This function reads test file
        and prints it to stdout
    """
    with open("UTF8", encoding='utf-8') as f:
        print(f.read(), end="")
