#!/usr/bin/python3
""" Module doc """


def say_my_name(first_name, last_name=''):
    """
    says your name how frakin cute
    Args:
        first_name: your name
        last_name: lkjdshfkjdshf
    Raises:
        TypeError: on the first
        TypeError: on the second
    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))


if __name__ == "__main__":
    from doctest import testfile
    testfile('tests/3-say_my_name.txt')
