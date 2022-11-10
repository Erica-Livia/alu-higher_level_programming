#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(), end="")
        return True
    except:
        return False
