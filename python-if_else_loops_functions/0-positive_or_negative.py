#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number>0:
        print(f'The number {number} is positive\n')
elif number<0:
        print(f'The number {number} is negative\n')
elif number==0:
    print('The number is 0\n')
