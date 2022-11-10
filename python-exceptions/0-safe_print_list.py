#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        elmt = 0
        if elmt < x:
            try:
                print("{}".format(my_list[i], end=""))
            except IndexError:
                break
            elmt = elmt + 1
        print()
        return elmt
