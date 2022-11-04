#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return(0)
    a = 0
    s = 0
    for i in my_list:
        a += (i[0] * i[1])
        s += i[1]
    return (a / s)
