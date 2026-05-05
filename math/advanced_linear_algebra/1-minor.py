#!/usr/bin/env python3
"""
Module to calculate the minor matrix
"""


def determinant(matrix):
    """
    Helper function for determinant calculation
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def minor(matrix):
    """
    Calculates the minor matrix of a square matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        row_res = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for row in (matrix[:i] + matrix[i + 1:])]
            row_res.append(determinant(sub))
        minor_matrix.append(row_res)

    return minor_matrix
