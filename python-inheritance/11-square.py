#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
