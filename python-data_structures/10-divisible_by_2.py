#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = []
    for i in my_list:
        if i % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
