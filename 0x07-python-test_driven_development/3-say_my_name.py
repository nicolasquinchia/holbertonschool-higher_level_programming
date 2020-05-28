#!/usr/bin/python3
"""This module contains a function that say hi to a specific name
    """


def say_my_name(first_name, last_name=""):
    """Function that print a name with first and last name

    Arguments:
        first_name {[str]} -- First Name
    Keyword Arguments:
        last_name {str} -- Last Name  (default: {""})

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        if first_name is "Doom" and last_name is "Slayer":
            print("Welcome great Slayer")
        else:
            print("My name is {:s} {:s}".format(first_name, last_name))
