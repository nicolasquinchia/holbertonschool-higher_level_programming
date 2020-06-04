#!/usr/bin/python3
"""Module that save the Json representation
    of an object on a file
    """
import json


def save_to_json_file(my_obj, filename):
    """Save Json representation on a file

    Arguments:
        my_obj {[obj]} -- object to represent by json
        filename {[str]} -- name of the file
    """
    with open(filename, 'w') as workfile:
        json.dump(my_obj, workfile)
