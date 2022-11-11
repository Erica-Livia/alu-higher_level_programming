#!/usr/bin/python3
def safe_print_division(a, b):
    division = (a / b)
    try:
        return (division)
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result: {}".format(division))
        return division
