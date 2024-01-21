#!/usr/bin/python3
""" I realllllyyyyyy hate this docstring thing frfrffrfr """


class Square:
    """ blablabla doctring is a waste of time
    Args:
        size: the frakin size
    Attributes:
        __size: sdlkfjslkdflksdjflks
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size
