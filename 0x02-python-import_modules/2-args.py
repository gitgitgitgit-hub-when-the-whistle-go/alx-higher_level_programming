#!/usr/bin/python3 
import sys
l = len(sys.argv)
print("{} arguments".format(l - 1), end="")
if l == 1:
    print(".")
else:
    print(":")
    for i in range(1, l):
        print("{}: {}".format(i, sys.argv[i]))
