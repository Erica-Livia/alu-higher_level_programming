#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elmt = 0
    for elmt in range(x):
        try:
            print("{:d}".format(my_list[elmt]), end="")
        except:
            continue
    print()
    return elmt
