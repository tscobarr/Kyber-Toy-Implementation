from poly import Polynomial

class PolynomialVector:
    def __init__(self, polynomials):
        self.polynomials = polynomials
        self.q = polynomials[0].q
        self.n = len(polynomials[0].coefficients)

    def __add__(self, other):
        if len(self.polynomials) != len(other.polynomials):
            raise ValueError("Vectors must have the same length")
        result = [self.polynomials[i] + other.polynomials[i] for i in range(len(self.polynomials))]
        return PolynomialVector(result)

    def __sub__(self, other):
        if len(self.polynomials) != len(other.polynomials):
            raise ValueError("Vectors must have the same length")
        result = [self.polynomials[i] - other.polynomials[i] for i in range(len(self.polynomials))]
        return PolynomialVector(result)

    def inner_product(self, other):
        if len(self.polynomials) != len(other.polynomials):
            raise ValueError("Vectors must have the same length")
        result = Polynomial([0] * self.n, self.q)
        for i in range(len(self.polynomials)):
            result = result + self.polynomials[i].mul_rq(other.polynomials[i], self.n)
        return result

    def __repr__(self):
        return "PolynomialVector({})".format(self.polynomials)