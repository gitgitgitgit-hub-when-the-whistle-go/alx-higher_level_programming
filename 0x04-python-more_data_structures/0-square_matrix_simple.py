def square_matrix_simple(matrix=[]):
    newmatrix = []
    for lis in matrix:
        ligne = []
        for e in lis:
            ligne.append(e ** 2)
        newmatrix = ligne
    return newmatrix
