#!/usr/bin/env python3
"""
Module to calculate the cofactor matrix of a matrix
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


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a matrix
    Args:
        matrix: list of lists whose cofactor matrix should be calculated
    Returns:
        The cofactor matrix of matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    # Special case for 1x1 matrix
    if n == 1:
        return [[1]]

    cofactor_matrix = []
    for i in range(n):
        row_cofactors = []
        for j in range(n):
            # Create submatrix by removing row i and column j
            sub_matrix = [row[:j] + row[j + 1:]
                          for row in (matrix[:i] + matrix[i + 1:])]
            
            # Minor calculation
            min_val = determinant(sub_matrix)
            
            # Apply cofactor sign: (-1)^(i+j)
            row_cofactors.append(min_val * ((-1) ** (i + j)))
            
        cofactor_matrix.append(row_cofactors)

    return cofactor_matrix
