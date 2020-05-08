#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = []
    for n in matrix:
        new_mtx.append(list(map(lambda x: x ** 2, n)))
    return new_mtx
