#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ rectangle class
        Attr:
            width: width private
            height: height private
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """ calculate the area for you because you don't know how to X """
        return self.width * self.height

    def perimeter(self):
        """ docstring """
        # if w or h is 0 then perimeter 0, just use area in one comparaison xD
        if self.area() != 0:
            return 2 * (self.width + self.height)
        return 0

    def __str__(self):
        """ blabla """
        if self.area() == 0:
            return ''
        row = '#' * self.width + '\n'
        mat = row * self.height
        # we need to remove the last \n apparently, we can use rstrip
        # rstrip remove the sequence from the ending of the string
        # default is space
        # I accidentally typed rsplit and there is a function rsplit xD
        # return mat.rstrip('\n')
        # but I prefere mine xD
        return mat[0:-1]
