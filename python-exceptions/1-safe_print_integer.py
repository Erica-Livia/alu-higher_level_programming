#!/usr/bin/python3
def safe_print_integer(value):
    elmt = 0
    for elmt in range(value)
        try:
            print("{:d}".format(), end="")
        except IndexError:
            elmt += 1
    print()
    return elmt
