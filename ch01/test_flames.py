import unittest
import flames1
from flames1 import flame

class Flames(unittest.TestCase):

    def test_flames(self):
        self.assertEqual(flame("sunil","sweety"),"enemy")