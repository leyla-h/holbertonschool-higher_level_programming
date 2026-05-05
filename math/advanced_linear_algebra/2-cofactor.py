#!/usr/bin/env python3
"""
Module to calculate the cofactor matrix
"""


def determinant(matrix):
    """
    Helper function to find matrix determinant
    """
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(len(matrix)):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)
    return det


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a square matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cofactor_matrix = []
    for i in range(n):
        row_res = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for row in (matrix[:i] + matrix[i + 1:])]
            minor_val = determinant(sub)
            row_res.append(minor_val * ((-1) ** (i + j)))
        cofactor_matrix.append(row_res)

    return cofactor_matrix
