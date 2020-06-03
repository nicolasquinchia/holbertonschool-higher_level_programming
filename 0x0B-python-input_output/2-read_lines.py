#!/usr/bin/python3
"""This Module holds a function to print
    n lines of a text file
    """


def read_lines(filename="", nb_lines=0):
    """This funtion print n lines of a txt file

    Keyword Arguments:
        filename {str} -- Name of the file (default: {""})
        nb_lines {int} -- Numer of lines to print (default: {0})
    """
    with open(filename) as in_file:
        lines = 0
        for line in in_file:
            lines += 1
        if nb_lines <= 0 or nb_lines >= lines:
            in_file.seek(0)
            for line in in_file:
                print(line, end="")
        else:
            in_file.seek(0)
            for line in range(nb_lines):
                n = in_file.readline()
                print(n)
