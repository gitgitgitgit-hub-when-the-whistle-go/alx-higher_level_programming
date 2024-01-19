#!/usr/bin/python3
def print_sorted_dictionary(dic):
    lis = [x for x in dic.keys()]
    lis.sort()
    for key in lis:
        print("{}: {}".format(key, dic[key]))
# Warning dic.keys() don't return a list. it return a dict keys weird thing
# use list comprenhsion or list(dic.keys())
