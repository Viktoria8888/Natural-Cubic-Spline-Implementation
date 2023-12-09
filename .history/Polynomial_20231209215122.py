import numpy as np
class Polynomial:
    def __init__(self, *coeffs)-> None: # from the biggest power to the smallest one
        self.coeffs = np.array(coeffs)
        self.degree = len(coeffs) - 1
    def __add__(self, other)->list:
        # Adjusting the coefficients
        max_degree = max(self.degree,other.degree)
        adj_coeffs1 = np.concatenate((np.zeros(max_degree - self.degree),self.coeffs))
        adj_coeffs1 = np.concatenate((np.zeros(max_degree - self.degree),other.coeffs))
        return adj_coeffs1 + adj_coeffs2
poly1 = Polynomial([1,2,3,4])
poly2 = Polynomial([20,30,40])
print((poly1 + poly2))
