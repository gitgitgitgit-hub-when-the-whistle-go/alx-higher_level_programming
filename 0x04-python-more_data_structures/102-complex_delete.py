#!/usr/bin/python3
def complex_delete(a_dict, value):
    a_dict_copy = a_dict.copy()
    for element in a_dict_copy:
        if a_dict[element] == value:
            del a_dict[element]
    return a_dict
