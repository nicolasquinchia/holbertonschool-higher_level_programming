#!/usr/bin/python3
"""Takes your Github credentials (username and password)
    and uses the Github API to display your id
    """
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    print(response.json().get('id'))
