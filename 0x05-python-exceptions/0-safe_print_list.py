#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    if my_list is None:
        return printed
    try:
        for e in range(x):
            print(my_list[e], end='')
            printed += 1
    except IndexError:
        return printed
    finally:
        print("")
        return printed
