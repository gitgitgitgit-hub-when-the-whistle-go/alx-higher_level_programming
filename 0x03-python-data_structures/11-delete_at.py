#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list

# if you use my_list = my_list[:idx] + my_list[idx + 1:]
# you change only the new list not the original list
# if you use a loop some problem may occur if idx is in the edges.
# del seems the only solution
