#!/usr/bin/python3
def func(a, b, c):
    if a < b:
        return c
    else:
        if c > b:
            return a + b
        else:
            return a * b - c
