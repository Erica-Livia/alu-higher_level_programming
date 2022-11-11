#!/usr/bin/python3
def safe_print_integer_err(value):
   from sys import stderr 
    try:
        print("{:d}".format())
        return True
    except:
        stderr.write("Exception: {}\n".format(err))
        return False
