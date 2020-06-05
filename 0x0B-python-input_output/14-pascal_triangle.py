#!/usr/bin/python3
"""This module holds a function
    with pascal's Triangle
    """


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal's triangle of n

    Arguments:
        n {[int]} -- size of pascal's triangle

    Returns:
        [list] -- lists of integers representing the triangle
    """
    triangle_list = []
    if n <= 0:
        return triangle_list
    else:
        for i in range(n):
            floor_list = []
            floor_list.append(1)
            for j in range(1, i):
                floor_list.append(
                    triangle_list[i - 1][j - 1] + triangle_list[i - 1][j])
            if i != 0:
                floor_list.append(1)
            triangle_list.append(floor_list)
        return triangle_list
