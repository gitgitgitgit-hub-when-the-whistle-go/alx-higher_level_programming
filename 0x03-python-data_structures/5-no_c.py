#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for e in my_string:
        if e == 'c' or e =='C':
            continue
        new = new + e
