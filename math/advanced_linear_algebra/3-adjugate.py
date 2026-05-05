#!/usr/bin/env python3
"""
Module to calculate the adjugate matrix of a matrix
"""


def determinant(matrix):
    """
    Helper to calculate the determinant
    """
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(len(matrix)):
        sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det


def cofactor(matrix):
    """
    Helper to calculate the cofactor matrix
    """
    n = len(matrix)
    if n == 1:
        return [[1]]

    cof_matrix = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for row in (matrix[:i] + matrix[i + 1:])]
            row_cof.append(determinant(sub) * ((-1) ** (i + j)))
        cof_matrix.append(row_cof)
    return cof_matrix


def adjugate(matrix):
    """
    Calculates the adjugate matrix of a matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if n == 1:
        return [[1]]

    cof_mat = cofactor(matrix)

    adj = []
    for j in range(n):
        adj.append([cof_mat[i][j] for i in range(n)])

    return adj
