#!/usr/bin/python3
"""This Module holds a function that insert
    a text into specific file
    """


def write_file(filename="", text=""):
    """Insert text into a file

    Keyword Arguments:
        filename {str} -- Name of the file to insert text (default: {""})
        text {str} -- Text to insert into the file (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, 'w') as workfile:
        return workfile.write(text)
