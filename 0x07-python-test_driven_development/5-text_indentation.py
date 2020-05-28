#!/usr/bin/python3
"""Module with a function that insert new lines
       with specific characters on a string
    """


def text_indentation(text):
    """Print text with new lines on specific Characters

    Arguments:
        text {[str]} -- string to print

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        p = text[i - 1]
        m = text[i]
        if not(m == " " and (p == ':' or p == '.' or p == '?' or p == ' ')):
            if m == ':' or m == '.' or m == '?':
                print("{:s}\n".format(m))
            else:
                print(m, end="")
