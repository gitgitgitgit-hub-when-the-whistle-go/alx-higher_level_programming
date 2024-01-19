#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.update({key: "blabla del and pop didn't works 3bad5me"})
    a_dictionary.pop(key)
    return a_dictionary
