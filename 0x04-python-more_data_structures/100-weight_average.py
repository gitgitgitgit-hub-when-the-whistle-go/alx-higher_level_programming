#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    bast = 0
    ma9am = 0
    for element in my_list:
        bast += element[0] * element[1]
        ma9am += element[1]
    return bast / ma9am
