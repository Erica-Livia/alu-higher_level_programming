#!/usr/bin/python3
"""Defines a function that add a new attribute
    to an object if it is possible
"""


def add_attribute(self, attr, val):
    """function that adds a new attribute to an objct
    if it is possible
    """
    if hasattr(self, '__dict__') is False:
        raise TypeError("can't add new attribute")
        __append__(attr)

    setattr(self, attr, val)
