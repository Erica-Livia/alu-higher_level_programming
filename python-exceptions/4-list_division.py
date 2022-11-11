#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    div_tab = []
    for i in range(list_lenght):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            div_tab.append(division)
    return div_tab
