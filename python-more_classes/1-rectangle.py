#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of a new rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width of  the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height musht be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    
