#!/usr/bin/python3
""" I realllllyyyyyy hate this docstring thing frfrffrfr """


class Square:
    """ blablabla docstring is a waste of time
    Args:
        size: the frakin size
    Attributes:
        __size: sdlkfjslkdflksdjflks
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """ dbfdlkjldkfjgldkfg """
        return self.__size ** 2

    @property
    def size(self):
        """ frakkkkkk docstring """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
