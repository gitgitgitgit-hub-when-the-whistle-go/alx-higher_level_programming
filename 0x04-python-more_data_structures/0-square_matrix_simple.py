#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for lis in matrix:
        ligne = []
        for e in lis:
            ligne.append(e ** 2)
        newmatrix.append(ligne)
    return newmatrix
