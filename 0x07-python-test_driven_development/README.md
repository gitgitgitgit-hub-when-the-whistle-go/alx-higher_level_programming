inside the documentation for each funcion we can add 

def func():
    """
    >>> func('somethingwrong')
    TRaceback blbabalbalbalbalb
    ...
    Error: there was an error (copy it from the interpreter xD)

    don't forget the test for missing arguments

and then at the end of our file we add:

if __name__ == "__main__":
    import doctest
    doctest.testmod()

if all the test are good nothing is printed, otherwise, the failed test is printed
newlines don't between tests don't affect the test result
testmod form doctest will look in docstring for test to test xD

to test our function we ca use:
python3 myfile.py
python3 -m myfile -v  # -v is for having a the details in case of everything succesful
python3 -m doctest -v myfile.py # here we invoc the module doctest and we don't need the if name == main block

we can write all the doctest in another file and then, in our module we add:
from doctest import testfile
    testfile('path/file.txt)

good example: 4-print_square.py

there is another way of testing called unittest:

import unittest
import outmodule    # or __import__
class Our_test(unittest.TestCase):  
    def my_test(self):
        self.assertEqual(func(args), result)
    # all the tests should be inside the class

if __name__ == "__main__":
    unittest.main()

For this one I have no clue why are we wrapping all of this in a class xD

this should be saved in a .py file

it can be either executed with python3 command or with python3 -m unittest testfile.py or without specifying the file unittest module can look for tests inside the active folder
if any questions about a function form Testcase: >>> help(unittest.Testcase.assertSetEquals) in python3 interpreter. Basically, RDFM


