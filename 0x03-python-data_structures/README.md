unlike strings, lists can be immutable. str[i] = 'd' will return an error while list won't
list = a copies only the adress, list = a[:] create another copy of a
to compare a variable to None do not do 'var == None', pycodestyle will return an error. 'var is None' is the correct comp
None don't have the same behaviour as empty list


Ressources:
https://docs.python.org/3/tutorial/datastructures.html