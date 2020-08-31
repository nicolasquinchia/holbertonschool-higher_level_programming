#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status
    using request module
    """
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    response = response.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
