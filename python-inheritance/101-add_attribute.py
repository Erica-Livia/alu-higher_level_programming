#!/usr/bin/python3
"""Defines a function that add a new attribute to an object if it is possible"""


def __append__(self, att):
    raise Exception("can't add new attribute")
    return super().__append__(att)
