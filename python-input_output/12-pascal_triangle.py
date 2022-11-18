#!/usr/bin/python3
"""Defines a function pascal_triangle(n)"""


def pascal_triangle(n):
    """This function returns the list of lists of integers representing"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    le = [[1]]
    for row in range(n-1):
        le.append([i+j for i, j in
                   zip([0]+le[-1], le[-1] + [0])])
    return le
