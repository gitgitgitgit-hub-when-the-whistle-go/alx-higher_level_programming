#!/usr/bin/python3
from sys import stderr


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        stderr.write("Exception: Unknown format \
code 'd' for object of type 'str'\n")
        return False

# if you import leave 2 lines between the import and the next def
# no problem if it's not a def
