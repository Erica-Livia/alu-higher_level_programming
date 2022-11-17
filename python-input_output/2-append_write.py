#!/usr/bin/python3
"""defines a function append_write(filename="", text="")"""


def append_write(filename="", text=""):
    """a function that appends a string
        at the end of a the file and returns
        the number of characters added
    """
    with open(filename, "a", encoding='utf-8')as f:
        return(f.write(text))
