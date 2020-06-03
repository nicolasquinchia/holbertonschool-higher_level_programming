#!/usr/bin/python3
"""This Module hols a function to read and print a txt file
    """


def read_file(filename=""):
    """Function that reads and prints a specific file

    Keyword Arguments:
        filename {str} -- Name of the file to read and print (default: {""})
    """
    with open(filename) as in_file:
        for line in in_file:
            print(line, end="")
