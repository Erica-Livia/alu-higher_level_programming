#!/usr/bin/python3
def safe_print_division(a, b):
    elmt = 0
    try:
        print("{}".format(elmt))
    except:
        break
    finally:
        return (a / b)
