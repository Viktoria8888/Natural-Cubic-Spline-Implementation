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
    def __eq__(self, other):
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
    def __pow__(self, n):
        if n == 0:
            return Polynomial(1)
        return (self ** (n-1)) * self

class PiecewisePoly(Polynomial):

    def __init__(self, poly_list, ranges):
        """
        Parameters
        -----------
        poly_list : list
            List of objects of Polynomial type
        ranges: list
            List of x values

        """
        self.poly_list = poly_list
        self.ranges = ranges
        self.numberOfRanges = len(ranges) - 1

    def __call__(self, x):
        # Looking for a cubic function that would correspond to the range
        for i in range(self.numberOfRanges):
            b = self.ranges[i]
            e = self.ranges[i+1]
            if b <= x and x <= e:
                return self.poly_list[i](x)
        raise ValueError

    def __str__(self):
        res_str = ''
        for i in range(self.numberOfRanges):
            b = self.ranges[i]
            e = self.ranges[i+1]
            res_str += f"{b} <= x <= {e}  :  "
            res_str += str(self.poly_list[i])
            res_str += '\n'

        return res_str
