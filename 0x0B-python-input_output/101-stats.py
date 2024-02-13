#!/usr/bin/python3
""" returns the stats of data by 101-generator """


# idea 1 was to store all status codes in a list and then utilize list.count
# to calculate how many code occured
# idea 2 was to store all in int variable with match statement, that means 8
# variable
# the final idea is this, to avoid creating all the variables we store them
# in a list; if code is in list occur++

import sys
import re
size = 0
status_occur = [0, 0, 0, 0, 0, 0, 0, 0]
status_code = ['200', '301', '400', '401', '403', '404', '405', '500']
pattern = '<(.*?)>'
line_number = 0
while True:
    line = sys.stdin.readline()
    match = re.search(pattern, line)
    size += int(match.group(4))
    status = match.group(3)
    for i in range(len(status_code)): # or range(8)
        if status == status_code:
            status_occur += 1
    line_number += 1
    if line_number % 10 == 0:
        print("File size: {}".format(size))
        for i in range(8):
            if status_occur[i]:
                print("{}: {}".format(status_code[i], status_occur[i]))
