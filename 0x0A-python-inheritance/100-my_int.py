#!/usr/bin/python3
""" rebel int with == and != inverted """


class MyInt(int):
    """ this class sound like me xD... JK """
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != int:
            raise TypeError
        # my raise do not work XD apparently python raise an error before 
        # mine maybe because I specified the supper class as int ?????
        self.__value = value

    def __eq__(self, other):
        if self.__value == other.__value:
            return False
        return True

    def __ne__(self, other):
        if self.__value == other.__value:
            return True
        return False


######## this code is not working, eq and ne are not overwritten ########