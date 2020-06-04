#!/usr/bin/python3
import json
"""This module hold a funtion that gives
    the json representation on a string
    """


def to_json_string(my_obj):
    """Give the JSON representation of an object

    Arguments:
        my_obj {[object]} -- object to represent by Json

    Returns:
        [str] -- The json representation of a file
    """
    return json.dumps(my_obj, sort_keys=True)
