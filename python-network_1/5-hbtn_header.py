#!/usr/bin/python3
"""5-hbtn_header.py"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    le = requests.get(url)
    la = le.headers.get('X-Request-Id')
    print(la)
