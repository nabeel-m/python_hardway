import unittest
import math
from sin import factorial, sin_angle

def math_sin(x):
    rad = math.radians(x)
    return math.sin(rad)

class SineVal(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_sinval(self):
        for x in range (0, 91):
            actual = sin_angle(x, 5)
            expected = math_sin(x)
            self.assertLessEqual(expected - actual, 0.001)
