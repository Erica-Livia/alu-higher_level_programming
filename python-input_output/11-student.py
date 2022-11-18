#!/usr/bin/python3
"""Class Student"""


class Student:
    """Student"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function retrieves a dictionary representation of a student instance"""

        if attrs is None:
            return self.__dict__
        else:
            le = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    le[item] = self.__dict__[item]
            return nary

    def reload_from_json(self, json):
        """This function replaces all attributes of the Student instance from json"""

        for key, value in json.items():
            setattr(self, key, value)
