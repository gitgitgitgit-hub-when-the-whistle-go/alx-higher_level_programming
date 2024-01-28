#!/usr/bin/python3
""" Class BaseGeometry """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        raise Exception('area() is not implemented')

    @classmethod
    def integer_validator(self, name, value):
        """ k ur legit """
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/7-base_geometry.txt')
