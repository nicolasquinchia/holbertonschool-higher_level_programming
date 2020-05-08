#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = []
    new_mtx = [[x**2 for x in num] for num in matrix]
    return new_mtx
