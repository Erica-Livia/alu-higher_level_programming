#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry():
    """BaseGeometry with area(self) function
    and integer_validator(self, name, value) function
    """

    def __init__(self):
        """initialization"""

    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value:
            name is always a string
            raise a TypeError exception, with the message <name> must be an integer
            raise a ValueError exception with the message <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
