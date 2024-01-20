#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        return False

# if you import leave 2 lines between the import and the next def
# no problem if it's not a def
