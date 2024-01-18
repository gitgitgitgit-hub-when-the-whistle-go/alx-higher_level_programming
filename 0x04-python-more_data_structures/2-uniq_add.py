#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list == []:
        return sum
    copy_list = my_list.copy()
    copy_list.sort()
    element, sum = copy_list[0], copy_list[0]
    for e in copy_list:
        if e != element:
            sum += e
            element = e
    return sum
