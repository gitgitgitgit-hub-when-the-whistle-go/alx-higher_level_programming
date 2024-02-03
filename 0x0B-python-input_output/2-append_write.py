#!/usr/bin/python3
""" a function that appends string to a text file (UTF8) and returns the\
number of characters written """


def append_write(filename='', text=""):
    """ whatever the modul doc is saying xD """
    with open(filename, 'a', encoding="utf-8") as f:
        chars_printed = f.write(text)
    return chars_printed
