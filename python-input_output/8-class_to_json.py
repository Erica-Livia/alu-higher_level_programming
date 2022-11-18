#!/usr/bin/python3
"""Def function class_to_json(obj)"""


def class_to_json(obj):
    """This ffunction returns a dictionary description
        with data structure for JSON serialization of an object
    """
    return obj.__dict__
