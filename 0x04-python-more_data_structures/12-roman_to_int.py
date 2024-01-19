#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    for e in roman_string:
        match e:
            case 'M':
                sum += 1000
            case 'D':
                sum += 500
            case 'C':
                sum += 100
            case 'L':
                sum += 50
            case 'X':
                sum += 10
            case 'V':
                sum += 5
            case 'I':
                sum += 1
            case _:
                return None
    return sum
