#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for e in range(len(list)):
            print("{:d}".format(list[e]), end='')
            if e != len(list) - 1:
                print(" ", end='')
        print("")
