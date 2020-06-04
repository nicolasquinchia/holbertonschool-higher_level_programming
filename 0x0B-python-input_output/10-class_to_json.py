#!/usr/bin/python3
"""This module returns a object
    as a dict.
    """


def class_to_json(obj):
    """funtion that returns the dict description with simple data structure

    Arguments:
        obj {[obj]} -- Object to convert into a data structure

    Returns:
        [dict] -- Simple data structure from the obj
    """
    return obj.__dict__
