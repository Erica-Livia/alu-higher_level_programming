#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in my_list:
        if 1 > max:
            max = i
    returm max
