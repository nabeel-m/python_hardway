import unittest
from matrixadd import matrix
from matrixadd import matrixadd

class add2matrix(unittest.TestCase):
    def test_matrixadd(self):
        self.assertListEqual(matrixadd([[1, 2], [1, 2]], [[2, 3], [4, 5]]),[[3, 5], [5, 7]])
        self.assertlistEqual(matrixadd([[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [1, 5, 6]]), [[3, 5, 7], [5, 10, 12]])