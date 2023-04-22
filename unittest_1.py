import unittest

def sumowanie(a,b):
    return a+b

class Test_Sumowanie(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1,2),3)
    def test_sum_with_negative_numbers(self):
        self.assertEqual(sum(-1,-2),-3)
if __name__ == '__main__':
    unittest.main()
