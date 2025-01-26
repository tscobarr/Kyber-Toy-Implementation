from poly import Polynomial
from vector import PolynomialVector

def symmetric_mod(value, q):
    return ((value + q // 2) % q) - q // 2

def infinity_norm_integer(value, q):
    return abs(symmetric_mod(value, q))

def infinity_norm_polynomial(poly):
    return max(infinity_norm_integer(c, poly.q) for c in poly.coefficients)

def infinity_norm_vector(vector):
    return max(infinity_norm_polynomial(p) for p in vector.polynomials)

def round_q(value, q):
    sym_value = symmetric_mod(value, q)
    if -q / 4 < sym_value < q / 4:
        return 0
    else:
        return 1