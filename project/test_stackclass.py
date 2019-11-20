import unittest
from stackclass import Stack


class StackTester(unittest.TestCase):

    def test_stack_init(self):
        s = Stack()
        s.push("raj")
        s.push("ram")
        
        self.assertEqual(s.size(),2)
        self.assertEqual(s.items,["raj","ram"])
        
        s.pop()
        
        self.assertEqual(s.items,["raj"])
        self.assertEqual(s.size(),1)

if __name__ == '__main__':
    unittest.main()