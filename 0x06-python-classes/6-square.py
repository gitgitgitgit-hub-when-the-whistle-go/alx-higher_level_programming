#!/usr/bin/python3
""" I realllllyyyyyy hate this docstring thing frfrffrfr """


class Square:
    """ blablabla docstring is a waste of time
    Args:
        size: the frakin size
    Attributes:
        __size: sdlkfjslkdflksdjflks
        __position: sdlkfjslkdfjslkfd
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """ dbfdlkjldkfjgldkfg """
        return self.__size ** 2

    def my_print(self):
        """ sdfsdfs lksdjflks j """
        if self.size == 0:
            print("")
            exit
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print("")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(position[1], int) \
                or not isinstance(position[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position
