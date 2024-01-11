#!/usr/bin/python3
def no_c(my_string):
    new = ""
    if my_string is not None:
        for e in my_string:
            if e == 'c' or e == 'C':
                continue
            new = new + e
    return new
