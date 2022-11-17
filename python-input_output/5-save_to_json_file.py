#!/usr/bin/python3
"""Defines a function save_to_json_file"""
import json

def save_to_json_file(my_obj, filename):
    """This function writes an Object to a text file 
        using JSON representation
    """

    with open(filename, "a", encoding='utf-8') as f:
        json.dumps(my_obj, f)
