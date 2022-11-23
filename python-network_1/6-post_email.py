#!/usr/bin/python3
"""6-post_email.py"""
import requests
from sys import argv


if __name__ == "__main__":
    resp = requests.post(argv[1], data={"email": argv[2]})
    print(resp.text)
