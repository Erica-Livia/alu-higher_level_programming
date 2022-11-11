#!/ur/bin/python3
"""Class Square"""


class Square:
    """Square"""

     def __init__(self, size=0):
        """Initialization of a new square"""
        self.__size = size

    @property
    def size(self):
        """Size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size mut be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self)
        """returns the area of the square"""
        return (self.__size * self.__size)
