#!/usr/bin/python3
""" no queen can attack another queen World peace achieved """


# no queen can attack means 2 can't be in the same row horizantally,
# vertically or in the same diagonal
#
# vertically: no 2 nots have the same x
# horizontally: no 2 nots have the same y
# diagonal: x = 2y - (2b - a) or x = 2y + (a + 2b)
# I resorted to write the equations this way to handle only integers no floats
#
# now we need to find a way to generate all sort of combinaison xDDD
def nqueens(N):
    