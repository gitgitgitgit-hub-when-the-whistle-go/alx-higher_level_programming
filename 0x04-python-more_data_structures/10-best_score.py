#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = None
    # max contains the key and not the max value
    for e in a_dictionary:
        if max is None:
            max = e
        if a_dictionary[e] > a_dictionary[max]:
            max = e
    return max
