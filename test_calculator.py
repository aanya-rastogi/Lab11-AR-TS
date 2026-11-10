import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-7,-2),-9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6, 4), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, 2), -3)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 1), 0)
        self.assertEqual(logarithm(5, 25), 2)
        self.assertEqual(logarithm(3, 27), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()