#!/usr/bin/python3
""" sub class of Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ we will nade a square off a Rectangle """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """ size ** 2 """
        return self.__size ** 2
