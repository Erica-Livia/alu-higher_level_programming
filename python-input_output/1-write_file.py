#!/usr/bin/python3
"""Defines a function write_file(filename="", text="")"""


def write_file(filename="", text=""):
    """this function writes a string to a text file
        and returns the number of characters written
    """
    with open(filename, "a", encoding='utf-8') as f:
        return(f.write(text), end="")
