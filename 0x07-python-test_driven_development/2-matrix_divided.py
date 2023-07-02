#!/usr/bin/python3
"""
Module contains matrix_divided function that
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    The function divides all elements of a given matrix
    by a given number
    """
    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(col / div, 2) for col in row] for row in matrix]
