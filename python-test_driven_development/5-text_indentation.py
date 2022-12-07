#!/usr/bin/python3
"""This function will print a text with 2 new lines after '.', '?' and ':' """


def text_indentation(text):
    """prints text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    new = text.split("\n")
    print("\n".join(line.strip(" ") for line in new), end="")
