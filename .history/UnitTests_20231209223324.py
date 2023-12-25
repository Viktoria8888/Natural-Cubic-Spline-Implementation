import unittest
from Polynomial import Polynomial
import numpy as np
poly1 = Polynomial([1, 2, 3])
poly2 = Polynomial([20, 30, 40])
class TestPoly(unittest.TestCase):

    # def test_add(self):
    #     # x^2 + 2x+3 + (20x^2 + 30x + 40)
    #     result = poly1 + poly2
    #     expected_result = np.array([[21, 32, 43]])
    #     np.testing.assert_array_equal(result, expected_result)
    def test_call(self):
        self.assertEqual(poly1(1),6)

if __name__ == '__main__':

    unittest.main()
