#!/usr/bin/python3
def uppercase(str):
    for c in str:
        current = ord(c)
        if current > 96 and current < 123:
            current = current - 32
        print(chr(current), end='')
    print("")
