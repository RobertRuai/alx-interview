#!/usr/bin/python3
"""rotate_matrix module"""


def rotate_2d_matrix(matrix):
    """rotates matrix 90 degrees clockwise"""
    a = len(matrix)

    for i in range(a):
        for j in range(i + 1, a):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(a):
        matrix[i].reverse()
