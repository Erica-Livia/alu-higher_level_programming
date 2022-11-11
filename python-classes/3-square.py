#!/user/bin/python3
"""Class square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """Initialization of a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)
