import unittest
from Polynomial import *
from CubicSpilneFunctions import difference_quotient
poly1 = Polynomial(1, 2, 3)
poly2 = Polynomial(20, 30, 40)
class TestPoly(unittest.TestCase):

    def test_add(self):
        # x^2 + 2x+3 + (20x^2 + 30x + 40)
        result = poly1 + poly2
        expected_result = Polynomial(21, 32, 43)
        self.assertEqual(result, expected_result)
    def test_call(self):
        res = poly1(1)
        self.assertEqual(res,6)
    def test_mul(self):
        poly1 = Polynomial(1, 2, 3)
        mult_constant = 2 * poly1
        expected_result1 = Polynomial(2,4,6)

        mult_poly = poly1 * poly2
        expected_result2 = Polynomial(1,3,5,6)
        if mult_constant != expected_result1:
            print("mult_constant:", mult_constant)
            print("expected_result1:", expected_result1)
    def test_difference_quotient(self):
        res = difference_quotient([0,1,3,5],[0,1,27,125])
        self.assertEqual(res,1);

if __name__ == '__main__':

    unittest.main()
