#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenv = len(sys.argv)
    # plural or singular
    if lenv == 2:
        arg_args = "argument"
    else:
        arg_args = "arguments"
    print("{} {}".format(lenv - 1, arg_args), end="")
    if lenv == 1:
        print(".")
    else:
        print(":")
        for i in range(1, lenv):
            print("{}: {}".format(i, sys.argv[i]))
