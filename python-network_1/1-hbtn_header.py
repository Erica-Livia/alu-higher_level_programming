#!/usr/bin/python3
"""1-hbtn_header.py"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        data = response.getheader('X-Request-Id')
        print(data)
