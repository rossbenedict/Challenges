import unittest
from Fibonacci import *
from ConvertToString import *
from SplitWord import *

class Challenge4(unittest.TestCase):

    def test_challenge4fibonacci(self):
        print(Fibonacci(9))
        print(ConvertToString(103123))


if __name__ == '__main__':
    unittest.main()
