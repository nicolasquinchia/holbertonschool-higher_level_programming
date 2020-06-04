#!/usr/bin/python3
"""This module holds a funtion to create
    object from a json file
    """
import json


def load_from_json_file(filename):
    """Create object from a JSON file

    Arguments:
        filename {[str]} -- name of the json file

    Returns:
        [object] -- Python data structure, object.
    """
    with open(filename, 'r') as workfile:
        new_object = json.load(workfile)
        return new_object
