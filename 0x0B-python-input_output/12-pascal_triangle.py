#!/usr/bin/python3
""" function to generate a pascal triangle """


def pascal_triangle(n):
    """ function that creates a pascal triangle
    Args:
        - int n: number of rows of the triangle
    """
    if n <= 0:
        return []

    pascal_tri = [[1]]
    for x in range(1, n):
        prev = pascal_tri[-1]
        new = [1]
        for y in range(1, x):
            new.append(prev[y - 1] + prev[y])

        new.append(1)
        pascal_tri.append(new)
    return pascal_tri
