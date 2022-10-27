#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if "{:c}".format(i) == 'e' or "{:c}".format(i) == 'q':
        continue
    else:
        print("{c}".format(i))
