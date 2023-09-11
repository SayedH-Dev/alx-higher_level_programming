#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for array in matrix:
            for i in array:
                    print("{:d}".format(i), end=" ")
            print()
