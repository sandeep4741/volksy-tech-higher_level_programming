#!/usr/bin/python3
""" 1. Divide a matrix """


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix"""
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for lists in matrix:
        if isinstance(lists, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(lists) is 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(lists) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have "
                            "the same size")
        for elmts in lists:
            if isinstance(elmts, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(elmts/div, 2) for elmts in lists] for lists in matrix]
