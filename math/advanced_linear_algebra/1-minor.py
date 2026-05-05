#!/usr/bin/env python3
"""
Module to calculate the minor matrix of a matrix
"""


def determinant(matrix):
    """
    Helper function to calculate the determinant of a matrix
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


def minor(matrix):
    """
    Calculates the minor matrix of a matrix
    Args:
        matrix: list of lists whose minor matrix should be calculated
    Returns:
        The minor matrix of matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check for empty matrix or non-square matrix
    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    # Special case for 1x1 matrix: the minor is defined as 1
    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            # Create submatrix by removing row i and column j
            sub_matrix = [row[:j] + row[j + 1:]
                          for row in (matrix[:i] + matrix[i + 1:])]
            row_minors.append(determinant(sub_matrix))
        minor_matrix.append(row_minors)

    return minor_matrix
