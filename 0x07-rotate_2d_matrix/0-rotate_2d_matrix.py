#!/usr/bin/python3
"""
A 90 degree rotation function
"""


def rotate_2d_matrix(matrix):
    """
    Rotating a 2D matrix using offset and layers
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top
