import unittest
import math
from calculator import square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(math.e), 1, places=5)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

if __name__ == "__main__":
    unittest.main()
