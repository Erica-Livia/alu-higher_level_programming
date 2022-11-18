#!/usr/bin/python3
"""Class Student"""


class Student:
    """Student"""

    def __init__(self, first_name, last_name, age):
        """Initialiation"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """This function retrieves a dictionary
            representation of a Student instance
        """
        return self.__dict__
