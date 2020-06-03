#!/usr/bin/python3
"""This Module holds a funtion to read and count
    the lines of a txt file
    """


def number_of_lines(filename=""):
    """Funtion to count the lines of a file

    Keyword Arguments:
        filename {str} -- Name of the file (default: {""})

    Returns:
        [int] -- Number of lines counted
    """
    with open(filename) as in_file:
        lines = 0
        for line in in_file:
            lines += 1
        return lines
