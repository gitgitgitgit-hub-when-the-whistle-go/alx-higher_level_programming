#!/usr/bin/python3
""" a sub class of list that have a print_sorted method """


class MyList(list):
    """  as said in the module docstring """
    def __init__(self):
        pass

    def print_sorted(self):
        """ print the list in a sorted way xD """
        for e in self:
            if not isinstance(e, int):
                raise TypeError
        copy_list = self.copy()
        copy_list.sort()
        print(copy_list)
