import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-7,-2),-9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(6, 4), 2)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(-1, 2), -3)

    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 1), 0)
        self.assertEqual(log(5, 25), 2)
        self.assertEqual(log(3, 27), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0, 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()