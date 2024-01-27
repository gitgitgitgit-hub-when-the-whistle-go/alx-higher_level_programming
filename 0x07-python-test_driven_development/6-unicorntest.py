import unittest

ut = __import__('6-unicorn').unicorn_test

class test_of_the_unicorn:
    def test_int(self):
        self.assertRaise(ut(10), TypeError)

if __name__ == '__main__':
    unittest.main()
