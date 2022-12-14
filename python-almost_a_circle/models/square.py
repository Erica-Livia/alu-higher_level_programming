#!/usr/bin/python3
"""Class Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square
        Attr, id = number,
        size = number,
        x =  number and y = number"""

    def __init__(self, size, x=0, y=0, id=None):
