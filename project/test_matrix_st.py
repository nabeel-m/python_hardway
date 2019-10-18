import unittest

from matrix_st import matrix_add

class MatrixAddTest(unittest.TestCase):
    def test_add(self):
        m1 = [[1]]
        m2 = [[1, 2],
              [3, 4]]

        result, err = matrix_add(m1, m2)
        __import__('ipdb').set_trace()
        self.assertFalse(err, "should fail" )
