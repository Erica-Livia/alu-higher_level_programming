#!/usr/bin/python3
"""Defines a function that add a new attribute to an object if it is possible"""


def __append__(self, att):
    """function that adds a new attribute to an objct
    if it is possible
    """
    raise Exception("can't add new attribute")
    return super().__append__(att)
