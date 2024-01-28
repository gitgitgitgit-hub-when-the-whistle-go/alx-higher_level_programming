If we create 2 exact strings or 2 exact integers, python will create only one instance to optimize resources usage. Only after we modify one of them he will create a second one.
To clone a list: list[:] or list.copy()
to have address (called the variable identifier in pycthon) of an object : id()
to have the type of an object: type()
in 18 task: the function creates duplicates of each list and thus, the original ones are not modified 