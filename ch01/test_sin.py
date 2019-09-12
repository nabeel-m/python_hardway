import unittest
from sin import factorial
from sin import sinval

class SineVal(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4),24)

    def test_sinval(self):
        self.assertEqual(sinval(90,20),1.0)        