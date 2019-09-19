import unittest
from math import sin
from sin import factorial
from sin import sinval

class SineVal(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4),24)

    def test_sinval(self):
        for x in range (0,91):
            self.assertEquals(sinval(x,20),sin(x))
            #self.assertEqual(sinval(45,20),sin(45))        