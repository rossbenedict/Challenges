import unittest
from Fibonacci import *
from ConvertToString import *

class Challenge4(unittest.TestCase):

    def test_challenge4fibonacci(self):
        print(Fibonacci(9))
        print(ConvertToString(123123))


if __name__ == '__main__':
    unittest.main()





#Premise of challenge 4
#
# creating our own methods
#
# make a fibonacchi sequence
#  0,1,1,2,3,5,8
#
#  Python Fibonacchi  can be copied from others