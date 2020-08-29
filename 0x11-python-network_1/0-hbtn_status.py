#!/usr/bin/python3
"""Module that fetches https://intranet.hbtn.io/status
    """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- type: {}".format(html.decode('utf-8')))
