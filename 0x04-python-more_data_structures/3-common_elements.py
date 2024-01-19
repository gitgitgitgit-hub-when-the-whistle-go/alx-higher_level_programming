#!/usr/bin/python3
def common_elements(set_1, set_2):
    lis = []
    for e in set_1:
        for f in set_2:
            if e == f:
                lis.append(e)
                break
    return set(lis)
