#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    for e in my_list:
        if e % 2 == 0:
            div.append(True)
        else:
            div.append(False)
    return div
