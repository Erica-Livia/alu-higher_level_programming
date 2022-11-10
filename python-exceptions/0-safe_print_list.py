#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elmt in range(x)
            print("{}".format(my_list[elmt], end=""))
        print()
        return x
    except IndexError:
        print()
        return elmt
