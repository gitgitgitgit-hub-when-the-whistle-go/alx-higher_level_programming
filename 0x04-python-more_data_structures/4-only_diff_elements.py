#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lis1 = [x for x in set_1 if x not in set_2]
    lis2 = [x for x in set_2 if x not in set_1]
    lis1.extend(lis2)
    return lis1
# lol I forgot about in and not in and list comprehension xD
