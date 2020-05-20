#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square that defines a square.
    Attributes:
        size - instance private: The size of a square
    Erros:
        TypeError - must be an integer
        ValueError - must be greather than zero
    """

    """
    Method to initialize an object or instance
    and check if there are any kind of error.
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
