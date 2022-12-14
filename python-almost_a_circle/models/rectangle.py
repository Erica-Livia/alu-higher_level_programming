#!/bin/usr/python3
"""Class Rectangle"""
from models.base import base


class Rectangle(Base):
    """Rectangle 
       Attr: id, width, height, x and y
    """

    def __init_(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
