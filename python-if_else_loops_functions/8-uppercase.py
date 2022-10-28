#!/usr/bin/python3
def uppercase(a):
    for c in a:
        if 123 > ord(c) > 96:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print('')
