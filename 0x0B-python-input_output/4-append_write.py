#!/usr/bin/python3
"""This module holds a funtion
    to append text on a specific file
    """


def append_write(filename="", text=""):
    """Append text in a specific file returning
    the numer of characters writen

    Keyword Arguments:
        filename {str} -- Name of the file where texts is append(default: {""})
        text {str} -- string to append on the file (default: {""})

    Returns:
        [int] -- number of character writen on the file
    """
    with open(filename, 'a') as workfile:
        return workfile.write(text)
