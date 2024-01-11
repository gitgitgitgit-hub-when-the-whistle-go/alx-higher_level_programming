#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for e in list:
            print("{:d}".format(e), end='')
        print("")
