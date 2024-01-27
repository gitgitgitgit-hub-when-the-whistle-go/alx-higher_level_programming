import unittest

ut = __import__('6-unicorn').unicorn_test

class test_of_the_unicorn(unittest.TestCase):
    def test_int(self):
        with self.assertRaises(TypeError):
            ut(10)

    def test_returm(self):
        self.assertAlmostEquals(ut('fdsf'), 10)

if __name__ == '__main__':
    unittest.main()

# call it with python3 -m unittest tests/6-unicorntest.py fron previous folder
