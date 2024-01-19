#!/usr/bin/python3
def roman_to_int(roman_string):
    lis1 = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    lis2 = [1000, 500, 100, 50, 10, 5, 1]
    temp = 0
    sum = 0
    old = 999
    for e in roman_string:
        # looking for pos in lis1
        i = 0
        while i < len(lis1):
            if lis1[i] == e:
                pos = i
                break
            i += 1
        if i == len(lis1):
            # print("character unkown: {}".format(e))
            return None
        # if we are just getting started
        if old == 999:
            old = i
        # what should be done
        if old - i < 0:
            sum += temp
            temp = lis2[i]
        elif old - i == 0:
            temp += lis2[i]
        elif old - i > 0:
            sum = lis2[i] - temp
            temp = 0
        # current become old, you can't stay young forever
        old = i
    # we add what is left of temp because we reached the end of our text
    sum += temp
    return sum


# I tried to remove the occurences like VM or VD by setting a difference
# old - i of 1. it removes VM and allows IV but blocks IX.
# For that purpose I worked with a list instead of a dictionary (to set order
# between letters) but in the end it did not serve that purpose
# Further documentation should be done to have an exhaustive list of what
# passes and what do not.
# lel roman orthographe is not that easy xDDD
