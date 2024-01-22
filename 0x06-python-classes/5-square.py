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

    def my_print(self):
        """ sdfsdfs lksdjflks j """
        if self.size == 0:
            print("")
            return None
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
