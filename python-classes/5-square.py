#!/usr/bin/python3
"""Class Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """Initialization of a new square"""
        self.__size = size

    @property
    def size(self):
        """Size of the Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= )")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """it will print thr square with the #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
