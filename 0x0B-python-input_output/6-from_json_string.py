#!/usr/bin/python3
"""This Module holds a funtion to decodificate with json
    """
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string

    Arguments:
        my_str {[str]} -- string to represent in object

    Returns:
        [obj] -- Python data structure, object
    """
    return json.loads(my_str)
