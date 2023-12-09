import unittest
from Polynomial import Polynomial
class TestPoly(unittest.TestCase):

    def test_add(self):
        # x^2 + 2x+3 + (20x^2 + 30x + 40)
        poly1 = Polynomial([1,2,3])
        poly2 = Polynomial([20,30,40])
        self.assertEqual((poly1 + poly2), [22,32,42])

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
