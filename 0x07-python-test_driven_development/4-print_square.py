#!/usr/bin/python3
"""
This module holds a function that prints a square with the character #.
"""


def print_square(size):
    """Function that prints a square of certain size

    Arguments:
        size {[int]} -- size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
