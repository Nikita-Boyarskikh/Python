import unittest

def sum_(x,y):
    return x+y

class UserTest(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(sum_(1,2) == 3)

unittest.main()
