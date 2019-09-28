import unittest
from program_py import factorial

class TestFactorial(unittest.TestCase):
    def test_init(self):
        a=4
        result=factorial(a)
        self.assertEqual(result,24)

if __name__ == '__main__':
    unittest.main()        
