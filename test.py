import unittest
from poly import Polynomial
from vector import PolynomialVector
from norms import infinity_norm_integer, infinity_norm_polynomial, infinity_norm_vector, round_q

class TestPolynomial(unittest.TestCase):
    def test_addition(self):
        q = 17
        p1 = Polynomial([5, 0, 4, 3], q)
        p2 = Polynomial([6, 3, 2, 0], q)
        result = p1 + p2
        expected = Polynomial([11, 3, 6, 3], q)
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_subtraction(self):
        q = 17
        p1 = Polynomial([5, 0, 4, 3], q)
        p2 = Polynomial([6, 3, 2, 0], q)
        result = p1 - p2
        expected = Polynomial([-1 % q, -3 % q, 2, 3], q)
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_multiplication(self):
        q = 7
        p1 = Polynomial([5, 0, 4, 3], q)
        p2 = Polynomial([6, 3, 2, 0], q)
        result = p1 * p2
        expected = Polynomial([2, 1, 6, 2, 3, 6, 0], q)
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_mul_rq(self):
        q = 41
        p1 = Polynomial([32, 0, 17, 22], q)
        p2 = Polynomial([11, 7, 19, 1], q)
        n = 4
        result = p1.mul_rq(p2, n)
        expected = Polynomial([39, 35, 35, 24], q)
        self.assertEqual(result.coefficients, expected.coefficients)

class TestPolynomialVector(unittest.TestCase):
    def test_addition(self):
        q = 41
        p1 = Polynomial([32, 0, 17, 22], q)
        p2 = Polynomial([11, 7, 19, 1], q)
        p3 = Polynomial([5, 9, 3, 14], q)
        p4 = Polynomial([2, 6, 8, 10], q)
        v1 = PolynomialVector([p1, p2])
        v2 = PolynomialVector([p3, p4])
        result = v1 + v2
        expected = PolynomialVector([Polynomial([37, 9, 20, 36], q), Polynomial([13, 13, 27, 11], q)])
        self.assertEqual(result.polynomials[0].coefficients, expected.polynomials[0].coefficients)
        self.assertEqual(result.polynomials[1].coefficients, expected.polynomials[1].coefficients)

    def test_subtraction(self):
        q = 41
        p1 = Polynomial([32, 0, 17, 22], q)
        p2 = Polynomial([11, 7, 19, 1], q)
        p3 = Polynomial([5, 9, 3, 14], q)
        p4 = Polynomial([2, 6, 8, 10], q)
        v1 = PolynomialVector([p1, p2])
        v2 = PolynomialVector([p3, p4])
        result = v1 - v2
        expected = PolynomialVector([Polynomial([27, -9 % q, 14, 8], q), Polynomial([9, 1, 11, -9 % q], q)])
        self.assertEqual(result.polynomials[0].coefficients, expected.polynomials[0].coefficients)
        self.assertEqual(result.polynomials[1].coefficients, expected.polynomials[1].coefficients)

    def test_inner_product(self):
        q = 137
        a = PolynomialVector([
            Polynomial([93, 51, 34, 54], q),
            Polynomial([27, 87, 81, 6], q),
            Polynomial([112, 15, 46, 122], q)
        ])
        b = PolynomialVector([
            Polynomial([40, 78, 1, 119], q),
            Polynomial([11, 31, 57, 90], q),
            Polynomial([108, 72, 47, 14], q)
        ])
        result = a.inner_product(b)
        expected = Polynomial([93, 59, 44, 132], q)
        self.assertEqual(result.coefficients, expected.coefficients)

class TestNorms(unittest.TestCase):
    def test_infinity_norm_integer(self):
        q = 41
        value = 32
        result = infinity_norm_integer(value, q)
        expected = 9
        self.assertEqual(result, expected)

    def test_infinity_norm_polynomial(self):
        q = 41
        p = Polynomial([32, 0, 17, 22], q)
        result = infinity_norm_polynomial(p)
        expected = 19
        self.assertEqual(result, expected)

    def test_infinity_norm_vector(self):
        q = 41
        p1 = Polynomial([32, 0, 17, 22], q)
        p2 = Polynomial([11, 7, 19, 1], q)
        v = PolynomialVector([p1, p2])
        result = infinity_norm_vector(v)
        expected = 19
        self.assertEqual(result, expected)

    def test_round_q(self):
        q = 41
        value = 32
        result = round_q(value, q)
        expected = 0
        self.assertEqual(result, expected)

    def test_round_q_polynomial(self):
        q = 3329
        p = Polynomial([3000, 1500, 2010, 37], q)
        rounded_coefficients = [round_q(c, q) for c in p.coefficients]
        result = Polynomial(rounded_coefficients, q)
        expected = Polynomial([0, 1, 1, 0], q)
        self.assertEqual(result.coefficients, expected.coefficients)

if __name__ == '__main__':
    unittest.main()