#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for e in range(x):
            print("{:d}",format(my_list[e]), end='')
            printed += 1
    except Exception:
        return printed
    finally:
        print("")
        return printed
