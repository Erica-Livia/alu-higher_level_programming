#!/usr/bin/python3
"""10-my_github.py"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    resp = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(resp.json().get('id'))
