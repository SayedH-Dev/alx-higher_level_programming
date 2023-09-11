def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        if not array:
            print()
        for i in array:
            print("{:d}".format(i), end=" ")
        print()
