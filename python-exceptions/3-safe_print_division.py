#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return (a / b)
    except:
        break
    finally:
        print("Inside result: {}".format(a / b))
        return (a / b)
