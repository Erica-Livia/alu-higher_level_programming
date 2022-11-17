#!/usr/bin/python3
"""defines a function read_file(filename="")"""


def read_file(filename="UTF8"):
    """This function reads test file
        and prints it to stdout
    """
    with open("UTF8") as f:
        for line in f:
            print(line, end="")
