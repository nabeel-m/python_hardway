def factorial(a):
        fact=1
        for i in range(1,a+1):
                fact=fact*i
        return fact

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(factorial(5),120)