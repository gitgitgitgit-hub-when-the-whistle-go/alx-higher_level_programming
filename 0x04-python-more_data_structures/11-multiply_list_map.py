#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    func = lambda x: x * number
    return list(map(func, my_list))
