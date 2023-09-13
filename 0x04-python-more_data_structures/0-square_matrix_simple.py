#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for array in matrix:
        squared = []
        for num in array:
            squared.append(num ** 2)
        result.append(squared)
    return result
