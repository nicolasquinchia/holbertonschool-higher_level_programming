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
        prev = text[i - 1]
        if not(text[i] == " " and (prev == ':' or prev == '.' or prev == '?' or prev == ' ')):
            if text[i] == ':' or text[i] == '.' or text[i] == '?':
                print("{:s}\n".format(text[i]))
            else:
                print(text[i], end="")
