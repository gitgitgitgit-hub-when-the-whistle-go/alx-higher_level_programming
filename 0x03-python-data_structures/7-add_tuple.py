#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = ()
    x = tuple_a
    y = tuple_b
    while len(x) < 3:
        x += (0,)
    while len(y) < 3:
        y += (0,)
    return x[0] + y[0], x[1] + y[1]

# .copy and .append don't work on tuple. <aybe all the list methods??
# to append use += tuple. be careful (11) is not a tuple (11, ) is one.
