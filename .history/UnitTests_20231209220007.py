import unittest
from Polynomial import Polynomial
import numpy as np

class TestPoly(unittest.TestCase):

    def test_add(self):
        # x^2 + 2x+3 + (20x^2 + 30x + 40)
        poly1 = Polynomial([1, 2, 3])
        poly2 = Polynomial([20, 30, 40])
        result = poly1 + poly2
        expected_result = np.array([[22, 32, 43]])  # Reshape to (1, 3)

        np.testing.assert_array_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()
