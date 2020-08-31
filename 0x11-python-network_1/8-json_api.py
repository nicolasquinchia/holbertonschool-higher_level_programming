#!/usr/bin/python3
"""Takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the
    letter as a parameter and check the JSON body
    response
    """
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        values = {'q': argv[1]}
    else:
        values = {'q': ""}
    response = requests.post(url, data=values)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except TypeError:
        print("Not a valid JSON")
