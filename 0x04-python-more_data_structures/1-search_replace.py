#!/usr/bin/python3
def search_replace(my_list, search, replace):
    l = len(my_list)
    for i in range(l):
        if my_list[i] == search:
            my_list[i] = replace
        