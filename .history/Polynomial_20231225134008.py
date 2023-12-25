import numpy as np

class Polynomial:
    def __init__(self, *coeffs):
        if type(coeffs) == list:
            raise ValueError
        self.coeffs = np.array(coeffs)
        self.degree = len(coeffs) - 1

    def __add__(self, other):
        max_degree = max(self.degree, other.degree)
        adj_coeffs1 = np.pad(self.coeffs, (max_degree - self.degree, 0), 'constant')
        adj_coeffs2 = np.pad(other.coeffs, (max_degree - other.degree, 0), 'constant')
        return adj_coeffs1 + adj_coeffs2

    def __call__(self, arg):
        res = 0
        for i, c in enumerate(self.coeffs):
            res += c * (arg ** (self.degree - i))
        return res
    def __str__(self):
        res = ""
        for i,c in enumerate(self.coeffs[:-1]):
            if c!=1 and c!=0:
                res+=f"{c}x^{i} + "
            elif c == 1:
                res+=f"x^{i} + "

        res+= str(self.coeffs[-1])
        return res
poly1 = Polynomial(1,2,3,5)

print(poly1)

# poly1 = Polynomial(1,2,3)
# res = poly1(1)
# print(res)
