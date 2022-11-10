#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        elmt = 0
        for elmt in range(x):
            try:
                print("{}".format(my_list[elmt]))
            except IndexError:
                break
            elmt += 1
            print()
        return elmt
