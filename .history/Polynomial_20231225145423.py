import numpy as np

class Polynomial:
    def __init__(self, *coeffs):
        """
        Parameters: coefficients sorted decreasingly based on power of x \n
        Ex. 3x^3 + 4x^2 -> Polynomial(3,4)
        """
        if type(coeffs) == list:
            raise ValueError
        self.coeffs = np.array(coeffs)
        self.degree = len(coeffs) - 1

    def __add__(self, other):
        max_degree = max(self.degree, other.degree)
        adj_coeffs1 = np.pad(self.coeffs, (max_degree - self.degree, 0), 'constant')
        adj_coeffs2 = np.pad(other.coeffs, (max_degree - other.degree, 0), 'constant')
        return Polynomial(*(adj_coeffs1 + adj_coeffs2))

    def __call__(self, arg):
        res = 0
        for i, c in enumerate(self.coeffs):
            res += c * (arg ** (self.degree - i))
        return res
    def __str__(self):
        res = ""
        for i,c in enumerate(self.coeffs[:-1]):
            i = self.degree - i
            if c!=1 and c!=0:
                res+=f"{c}x^{i} + "
            elif c == 1:
                res+=f"x^{i} + "

        res+= str(self.coeffs[-1])
        return res
    if self.coeffs.shape != other.coeffs.shape:
            return False
        return np.allclose(self.coeffs, other.coeffs)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_coeffs = self.coeffs * other
            return Polynomial(*new_coeffs)
        elif isinstance(other, Polynomial):
            result_coeffs = np.zeros(self.degree + other.degree + 1)
            for i in range(self.degree + 1):
                for j in range(other.degree + 1):
                    result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
            return Polynomial(*result_coeffs)
        else:
            raise TypeError("Unsupported type for multiplication")
    def __rmul__(self, other):
        return self * other



poly1 = Polynomial(1,1,3)
poly2 = Polynomial(1,2)
print(poly1*poly2)
