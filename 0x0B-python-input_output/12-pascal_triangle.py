#!/usr/bin/python3
""" returns list of pascal triangle """


def pascal_triangle(n):
    pascal = []
    if type(n) is not int:
        raise TypeError('a number is required')
    if n <= 0:
        return pascal
    if n == 1:
        pascal.append([1])
        return pascal
    if n >= 2:
        pascal.extend([[1], [1, 1]])
    for i in range(2, n):
        actual = [1]
        actual.extend([pascal[-1][j] + pascal[-1][j + 1]
                       for j in range(len(pascal[-1]) - 1)])
        actual.append(1)
        pascal.append(actual)
    return pascal
