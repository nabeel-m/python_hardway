import unittest
import math
from sin import factorial
from sin import sinval
from sin import sinangle

class SineVal(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4),24)

    def test_sinval(self):
        for x in range (0,91):
            self.assertLessEqual(sinval(x,20)-sinangle(x),0.01)
            #self.assertEqual(sinval(45,20),sin(45))        