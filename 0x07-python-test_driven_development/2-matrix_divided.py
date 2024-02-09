#!/usr/bin/python3
"""Defines a matrix."""


def matrix_divided(matrix, div):
    """Represent a new matrix."""
    
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    # Perform the division operation on each element of the matrix
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
