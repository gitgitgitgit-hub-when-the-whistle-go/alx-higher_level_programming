#!/usr/bin/python3
""" class student """


class Student:
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ from attribute dict to json """
        objdict = self.__dict__.copy()
        if type(attrs) is not list:
            return objdict
        for element in attrs:
            if type(element) is not str:
                return objdict
        if attrs == []:
            return objdict
        keys = list(objdict.keys())
        for k in keys:
            if k not in attrs:
                objdict.pop(k)
        return objdict
