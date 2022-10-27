#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if islower("{:c}".format(i)):
            return True
        else:
            return False
