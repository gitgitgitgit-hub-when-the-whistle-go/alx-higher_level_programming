#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenv = len(sys.argv)
    print("{} arguments".format(lenv - 1), end="")
    if lenv == 1:
        print(".")
    else:
        print(":")
        for i in range(1, lenv):
            print("{}: {}".format(i, sys.argv[i]))
