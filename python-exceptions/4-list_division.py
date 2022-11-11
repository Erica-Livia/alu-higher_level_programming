#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    elmt1 = 0
    elmt2 =0
    list_lenght = len(my_list_1, my_list_2)
    for i in range(list_lenght):
            try:
                division = my_list_1[i] / my_list_2[i]
            except:
                division = 0
            finally:
                if my_list_2[i] == 0:
                    print("division by 0")
                elif my_list_1[i] < my_list_2[i]:
                    print("out of range")
                elif (my_list_1[i], my_list_2[i]) in range(list_lenght)
                    print("wrong type")
                return division
