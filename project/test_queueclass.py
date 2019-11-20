import unittest
from queueclass import Queue


class QueueTester(unittest.TestCase):

    def test_queue(self):
        q = Queue()
        q.enqueue("raj")
        q.enqueue("ram")
        
        self.assertEqual(q.size(),2)
        self.assertEqual(q.items,["raj","ram"])
        
        q.dequeue()
        
        self.assertEqual(q.items,["ram"])
        self.assertEqual(q.size(),1)

if __name__ == '__main__':
    unittest.main()