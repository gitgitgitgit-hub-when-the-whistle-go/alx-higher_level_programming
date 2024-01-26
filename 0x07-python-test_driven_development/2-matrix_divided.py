#!/usr/bin/python3
""" Module doc """


def matrix_divided(matrix, div):
    """
    Args:
        matrix: a matrix xD ???
        div: it's self explanatory ffs
    Raises:
        TypeError: if element in matrix is not integer or float
        TypeError: if the matrix has rows not in the same size
        TypeError: if div is not int or float
        ZeroDivisionError: if div == 0
    Returns:
        a matrix with all the elemets form the original one divided by
        div rounded to 2 decimal
    """
    # we can see here that zerodiv and not integer errors can be checked while
    # the func is executing. let's check the 2 others at the beginning xD
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    # we need to check for matrix empty or None or priest
    if matrix is None or matrix == []:
        return None
    if not isinstance(matrix, list):
        raise Exception('it was at this moment Jackson knew... he fad up')
    lenght = len(matrix[0])
    for e in matrix:
        if len(e) != lenght:
            raise TypeError('Each row of the matrix must have the same size')

    # if we copy only the matrix and modify internal lists in the new mat
    # we will change also those in the original one so we need to copy them
    new_matrix = [lis.copy() for lis in matrix]
    for lis in new_matrix:
        for i in range(lenght):
            try:
                lis[i] = round(lis[i] / div, 2)
            except ZeroDivisionError:
                raise ZeroDivisionError('division by zero')
            except TypeError:
                # the only type error now is the one from dividing non integers
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
    return new_matrix


if __name__ == "__main__":
    from doctest import testfile
    testfile('tests/2-matrix_divided.txt')
