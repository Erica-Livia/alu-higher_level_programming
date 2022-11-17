#!/usr/bin/python3
"""Defines a function form_json_string(my_str)"""
import json


def from_json_string(my_str):
    """This function returns an object represented by a JSON string"""
    return json.dumps(my_str)
