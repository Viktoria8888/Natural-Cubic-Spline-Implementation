class Polynomial:
    def __init__(self, *coeffs)-> None: # from the biggest power to the smallest one
        self.coeffs = coeffs
        self.degree = len(coeffs) - 1
    def __add__(self, other)->list:
        # Adjusting the coefficients
        max_degree = max(self.degree,other.degree)
        adj_coeffs1 = [0]*(max_degree - self.degree) + list(self.coeffs)
        adj_coeffs2 = [0]*(max_degree - other.degree) + list(other.coeffs)
        res = list(map(lambda x,y: x+y, adj_coeffs1, adj_coeffs2))
        return res
poly1 = Polynomial([1,2,3])
poly2 = Polynomial([20,30,40])
print((poly1 + poly2))
