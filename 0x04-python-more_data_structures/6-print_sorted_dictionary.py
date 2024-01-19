#!/usr/bin/python3
def print_sorted_dictionary(dic):
    lis = dic.keys()
    lis.sort()
    for key in lis:
        print(dic[key])
