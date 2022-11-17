#!/usr/bin/python3
"""Defines a function read_file(filename=""):"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
