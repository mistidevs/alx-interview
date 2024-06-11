#!/usr/bin/python3
"""
A 90 degree rotation function
"""


def rotate_2d_matrix(matrix):
    """
    Rotating a 2D matrix using transposition and row reversal
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
