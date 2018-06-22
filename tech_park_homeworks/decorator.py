import unittest

LOG_FILE = 'log.txt'

class UserTest(unittest.TestCase):
    def setUp(self):
        @logger(LOG_FILE)
        def summator(nums):
            return sum(nums)
        self.fooname = 'summator'
        self.foo = summator
        self.res = 15
        self.args = (1,2,3,4,5)

    def test_res(self):
        self.assertEqual(self.foo(self.args), self.res)
    def test_log(self):
        with open(LOG_FILE, 'r') as f:
            a = f.read()
            self.assertEqual(a, 'function {} with arguments: {} returns {}'.format(self.fooname, self.args, str(self.res)))

def logger(file):
    def log(foo):
        def func(*args, **kwargs):
            result = foo(*args, **kwargs)
            with open(file, 'w') as f:
                f.write("function {} with arguments: {} returns {}".format(foo.__name__, args[0], str(result)))
            return result
        return func
    return log

if __name__ == '__main__':
    unittest.main()
