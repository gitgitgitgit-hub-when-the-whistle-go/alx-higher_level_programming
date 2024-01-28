If we create 2 exact strings or 2 exact integers, python will create only one instance to optimize resources usage. Only after we modify one of them he will create a second one.
To clone a list: list[:] or list.copy()
to have address (called the variable identifier in pycthon) of an object : id()
to have the type of an object: type()
in 18 task: the function creates duplicates of each list and thus, the original ones are not modified
l1 = []; l2 = []; l1 is l2  # True
list += list + otherlist  # here the list do not change address
list = list + otherlist  # here the list changes it address
To create a locked where the only attributes and method we use __slots__ = tuple of strings of what is authorized


hypothesis:
maybe when assigning an int value to a variable if we modify this variable and no other variable have that value python will discard this value and the variable will keep it adress otherwise the variable will move away in the memory. Long shot ???? let's find out XXDDDD
Answer:
This is false and you should stop applying philosophy in coding
Conclusion:
The value will hang arround in memory until the end of the program ?!!!?!?

Consider this example:
>>> a = [1,2]
>>> id(a)
140694918459200 
>>> a += [3,4,5]
>>> a
[1, 2, 3, 4, 5]
>>> id(a)
140694918459200
>>> b = [1,2,3,4,5,6,7,8,9,7,8,9,7,8,9,1]
>>> a += [3,4,5,6,75,2,3,5,4,6,2,1,5,9]
>>> for e in a:
...     actu = id(e)
...     print('{} >>> {} >>> {} >>> {}'.format(prev, actu, actu - p
rev, e))
...     prev = actu
... 
140694918459200 >>> 140694923182320 >>> 4723120 >>> 1
140694923182320 >>> 140694923the_only_attribute_possible" , "name", __dict__182352 >>> 32 >>> 2
140694923182352 >>> 140694923182384 >>> 32 >>> 3
140694923182384 >>> 140694923182416 >>> 32 >>> 4
140694923182416 >>> 140694923182448 >>> 32 >>> 5
140694923182448 >>> 140694923182384 >>> -64 >>> 3
140694923182384 >>> 140694923182416 >>> 32 >>> 4
140694923182416 >>> 140694923182448 >>> 32 >>> 5
140694923182448 >>> 140694923182480 >>> 32 >>> 6
140694923182480 >>> 140694923184688 >>> 2208 >>> 75
140694923184688 >>> 140694923182352 >>> -2336 >>> 2
140694923182352 >>> 140694923182384 >>> 32 >>> 3
140694923182384 >>> 140694923182448 >>> 64 >>> 5
140694923182448 >>> 140694923182416 >>> -32 >>> 4
140694923182416 >>> 140694923182480 >>> 64 >>> 6
140694923182480 >>> 140694923182352 >>> -128 >>> 2
140694923182352 >>> 140694923182320 >>> -32 >>> 1
140694923182320 >>> 140694923182448 >>> 128 >>> 5
140694923182448 >>> 140694923182576 >>> 128 >>> 9
>>> id(b) 
140694898250048
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 7, 8, 9, 1]
>>> a
[1, 2, 3, 4, 5, 3, 4, 5, 6, 75, 2, 3, 5, 4, 6, 2, 1, 5, 9]
>>> prev = id(b)
>>> for e in b:
...     actu = id(e)
...     print('{} >>> {} >>> {} >>> {}'.format(prev, actu, actu - prev, e))
...     prev = actu
... 
140694898250048 >>> 140694923182320 >>> 24932272 >>> 1
140694923182320 >>> 140694923182352 >>> 32 >>> 2
140694923182352 >>> 140694923182384 >>> 32 >>> 3
140694923182384 >>> 140694923182416 >>> 32 >>> 4
140694923182416 >>> 140694923182448 >>> 32 >>> 5
140694923182448 >>> 140694923182480 >>> 32 >>> 6
140694923182480 >>> 140694923182512 >>> 32 >>> 7
140694923182512 >>> 140694923182544 >>> 32 >>> 8
140694923182544 >>> 140694923182576 >>> 32 >>> 9
140694923182576 >>> 140694923182512 >>> -64 >>> 7
140694923182512 >>> 140694923182544 >>> 32 >>> 8
140694923182544 >>> 140694923182576 >>> 32 >>> 9
140694923182576 >>> 140694923182512 >>> -64 >>> 7
140694923182512 >>> 140694923182544 >>> 32 >>> 8
140694923182544 >>> 140694923182576 >>> 32 >>> 9
140694923182576 >>> 140694923182320 >>> -256 >>> 1

Observations:
If the list contains two equal ints then they are the same object
This goes beyond the list to include other lists, se can see that a and b contain some shared elemets
The list elements are not side by side, more like a linked list in C rather than an array.
32 bits to store ints on my machine
Even the first element is sometimes far from list's address
Even if b is declared after a b's address is before a, why ???