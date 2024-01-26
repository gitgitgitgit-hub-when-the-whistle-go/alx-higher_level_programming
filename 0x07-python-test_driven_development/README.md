inside the documentation for each funcion we can add 

def func():
    """
    >>> func('somethingwrong')
    TRaceback blbabalbalbalbalb
    ...
    Error: there was an error (copy it from the interpreter xD)
and then at the end of our file we add:
if __name__ == "__main__":
    import doctest
    doctest.testmod()
if all the test are good nothing is printed, otherwise, the failed test is printed
newlines don't between tests don't affect the test result

to test our function we ca use:
python3 myfile.py
python3 -m myfile -v  # -v is for having a the details in case of everything succesful
python3 -m doctest -v myfile.py # here we invoc the module doctest and we don't need the if name == main block


