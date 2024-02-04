#!/usr/bin/python3
""" append after the line containing the string """


def append_after(filename='', search_string='', new_string=''):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line)
    i = 0
    while i < len(lines):
        if search_string in lines[i]:
            i += 1
            lines.insert(i, new_string)
        i += 1
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
