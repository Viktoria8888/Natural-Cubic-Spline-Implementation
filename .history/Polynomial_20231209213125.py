class Polynomial:
    def __init__(self, *coeffs)-> None: # from the biggest power to the smallest one
        self.coeffs = coeffs
        self.degree = len(coeffs) - 1
    def __add__(self, other)->list:
        # Adjusting the coefficients
        max_degree = max(degree,other.degree)
        adj_coeffs1 = [0]*(max_degree - degree)
        adj_coeffs2 = [0]*(max_degree - other.degree)
        res = list(map(lambda x,y: x+y, adj_coeffs1, adj_coeffs2))
        return res
