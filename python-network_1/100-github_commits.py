#!/usr/bin/python3
"""100-github_commits.py"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            argv[2], argv[1])
    resp = requests.get(url)
    data = resp.json()
    for commit in data[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
