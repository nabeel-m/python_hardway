import unittest
from ch01 import fact

class Testfactorial(unittest.TestCase):
    def  test_fact(self):
        a=4
        result=fact(4)
        self.assertEqual(result,24)

if __name__ == '__main__':
    unittest.main()        