#!/usr/bin/python3

def unicorn_test(something):
    if isinstance(something, int):
        raise TypeError("I don't like int")
    print('unicorn')
    return 10
