#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ rectangle class
        Instance attrinutes:
            width: width private
            height: height private:
        Class attributes:
            number_of_instances: as the name suggests
            print_symbol: the char used to print our rektangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ dogstring """
        # if w or h is 0 then perimeter 0, just use area instead of 2 comp
        if self.area() != 0:
            return 2 * (self.width + self.height)
        return 0

    def __str__(self):
        """ blabla """
        if self.area() == 0:
            return ''
        # here I used self and not Rectangle because to each rect it symbol
        row = str(self.print_symbol) * self.width + '\n'
        mat = row * self.height
        # we need to remove the last \n apparently, we can use rstrip
        # rstrip remove the sequence from the ending of the string
        # default is space
        # I accidentally typed rsplit and there is a function rsplit xD
        # return mat.rstrip('\n')
        # but I prefere mine xD
        return mat[0:-1]

    def __repr__(self):
        """ like str but it's intended to be used by other functions
        Returns:
            Rectangle(w, h)
        >>> rektangle = eval(repr(rectangle))
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ customized delete """
        print("Bye rectangle...")  # you won't be remenbered xD
        # del is apparently a keyword like return so don't write del(self)
        # or pycodestyle will come and .... in your sleep
        del self
        Rectangle.number_of_instances -= 1
