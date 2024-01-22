#!/usr/bin/python3
""" I realllllyyyyyy hate this docstring thing frfrffrfr """


class Square:
    """ blablabla docstring is a waste of time
    Args:
        size: the frakin size
        position: tuple
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
        """ sdfsdfs lksdjflks jl """
        pos = self.position
        if self.size == 0:
            print("")
            return None
        print(pos[1] * "\n", end='')
        for i in range(self.size):
            print(pos[0] * " ", end='')
            for j in range(self.size):
                print("#", end='')
            print("")

    def __str__(self):
        """ sdfsdfs lksdjflks jl """
        prt = ""
        pos = self.position
        if self.size == 0:
            return prt
        prt += pos[1] * "\n"
        for i in range(self.size):
            prt += pos[0] * " "
            for j in range(self.size):
                prt += "#"
            prt += "\n"
        return prt

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
            raise TypeError('position must be a tuple of 2 positive integer')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integer')
        elif not isinstance(position[1], int) \
                or not isinstance(position[0], int):
            raise TypeError('position must be a tuple of 2 positive integer')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integer')
        self.__position = position
