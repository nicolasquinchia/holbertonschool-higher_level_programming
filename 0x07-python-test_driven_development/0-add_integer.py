#!/usr/bin/python3
"""
This module hold a function to add 2 numbers those must
be integers or floats
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers or floats

    Paramethers:
        a (float, int): The first value
        b (float, int): The second value. Defaults to 98.
    Errors:
        TypeError: if a is not a float or an int
        TypeError: if b is not a float or an int
    Returns:
        Integer with the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
