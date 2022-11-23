#!/usr/bin/python3
"""8-json_api.py"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        le = ""
    else:
        le = argv[1]
    dic = {"q": le}
    resp = requests.post('http://0.0.0.0:5000/search_user', data=dic)
    try:
        dic_1 = resp.json()
        if dic_1:
            print("[{}] {}".format(dic_1.get('id'), dic_1.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
