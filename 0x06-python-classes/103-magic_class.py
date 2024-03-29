#!/usr/bin/python3
""" the bladi docstring again """


import math


class magic_class:
    """ based on a python bytecode
    attrs:
            radius
    """
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ returns the area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ i hate docstring """
        return 2 * math.pi * self.__radius
