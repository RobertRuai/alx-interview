#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the pascal's triangle of n.
    """
    if (n <= 0):
        return []
    triangle = []
    row = []
    prev_row = []
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] + prev_row[j] or 1 for j in range(0, i)]
        prev_row = row
        triangle += [row]
    return triangle[1:]
