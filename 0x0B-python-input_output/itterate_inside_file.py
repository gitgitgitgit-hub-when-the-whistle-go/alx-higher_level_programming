#!/usr/bin/python3

def print_all_lines(filename):
    with open(filename, 'a+') as f:
        f.seek(0)
        line = f.read()
        print(line)
