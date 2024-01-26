#!/usr/bin/python3
""" module doc """


def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')
    for i in range(size):
        print(size * '#')


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/4-print_square.txt')
