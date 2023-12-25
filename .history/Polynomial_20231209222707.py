import numpy as np

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = np.array(coeffs)
        self.degree = len(coeffs) - 1

    def __add__(self, other):
        # Adjusting the coefficients
        max_degree = max(self.degree, other.degree)
        # Padding with zeros in front
        adj_coeffs1 = np.pad(self.coeffs, (max_degree - self.degree, 0), 'constant')
        adj_coeffs2 = np.pad(other.coeffs, (max_degree - other.degree, 0), 'constant')
        return adj_coeffs1 + adj_coeffs2

    def __call__(self, arg):
        res = 0
        for i, c in enumerate(self.coeffs):
            res += arg**(self.degree-i)*c
        return res
poly1 = Polynomial([1, 2, 3])
print(poly1(1))
