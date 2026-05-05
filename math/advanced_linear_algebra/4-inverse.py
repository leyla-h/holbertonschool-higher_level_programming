#!/usr/bin/env python3
"""
Module to calculate the inverse of a matrix
"""


def determinant(matrix):
    """
    Helper to calculate determinant
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)
    return det


def adjugate(matrix):
    """
    Helper to calculate adjugate matrix
    """
    n = len(matrix)
    if n == 1:
        return [[1]]

    cofactor_matrix = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for row in (matrix[:i] + matrix[i + 1:])]
            row_cof.append(determinant(sub) * ((-1) ** (i + j)))
        cofactor_matrix.append(row_cof)

    adj = [[cofactor_matrix[i][j] for i in range(n)] for j in range(n)]
    return adj


def inverse(matrix):
    """
    Calculates the inverse of a square matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)

    if det == 0:
        return None

    if n == 1:
        return [[1 / matrix[0][0]]]

    adj = adjugate(matrix)
    inv = [[elem / det for elem in row] for row in adj]

    return inv
