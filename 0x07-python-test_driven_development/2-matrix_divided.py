#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    Paramethers:
        matrix: list of lists of integers or floats
        div: number that divide all elements of a matrix
    Errors:
        TypeError: if matrix is not list
        TypeError: if the elements of the matrix are not
        a list
        TypeError: if any elements of the matrix is not
        a integer or float
        TypeError: if each row of the matrix is not the
        same size
        ZeroDivisionError: div can’t be equal to 0
    Returns:
        A new matrix with all elements divided by div
    """
    str_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or type(matrix) != list:
        raise TypeError(str_error)
    for i in matrix:
        if not i or type(i) != list:
            raise TypeError(str_error)
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(str_error)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for m in matrix:
            new_row = []
            for n in m:
                new_row.append(round(n / div, 2))
            new_matrix.append(new_row)
        return (new_matrix)
