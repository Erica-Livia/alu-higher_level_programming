#!/usr/bin/python3
"""This script adds all arguments to a Python list
    and then save them to a file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

f_name = "add_item.json"

try:
    data = load_from_json_file(f_name)
except FileNotFoundError:
    data = []

save_to_json_file(data + argv[1:], f_name)
