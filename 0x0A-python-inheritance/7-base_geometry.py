#!/usr/bin/python3
""" Class BaseGeometry """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ k ur legit """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/7-base_geometry.txt')
