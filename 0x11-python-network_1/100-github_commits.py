#!/usr/bin/env bash
from sys import argv
import requests
"""Check github commits, by repo and user
    """

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    for i in response.json()[0:10]:
        print("{}: {}".format(i.get('sha'), i.get(
            'commit').get('author').get('name')))
