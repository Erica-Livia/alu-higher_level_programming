#!/usr/bin/python3
"""defines a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file
        after each line containing a specific string
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        data = ""
        for line in f:
            data += line
            if search_string in line:
                data += new_string
        f.seek(0)
        f.write(data)
