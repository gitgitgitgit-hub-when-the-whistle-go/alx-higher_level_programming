#!/usr/bin/python3
""" modul doc """


def add_integer(a, b=98):
    """
    add to integers
    Args:
        a: first
        b: second
    Returns:
        a+b
    Raises:
        TypeError: if a or b NaN
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer or b must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('a must be an integer or b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    from doctest import testfile
    testfile('tests/0-add_integer.txt')
