#!/usr/bin/env python3
"""
Module to calculate the determinant of a matrix
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix
    Args:
        matrix: list of lists whose determinant should be calculated
    Returns:
        The determinant of matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    if len(matrix) == 0:
        return 1

    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        # Create submatrix by excluding the first row and the current column
        sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        # Recursive call to find the determinant of the submatrix
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)

    return det
