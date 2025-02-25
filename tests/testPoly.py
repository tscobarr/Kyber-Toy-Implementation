import unittest
from poly import Polynomial, PolynomialVector
from utils import compare_polynomials, compare_polynomial_vectors

class TestPolynomial(unittest.TestCase):
    def setUp(self):
        self.q = 41

    def test_add_polynomials(self):
        for _ in range(10):
            f1 = Polynomial.random_polynomial(10, self.q)
            zero = Polynomial([0], self.q)
            f2 = Polynomial.random_polynomial(10, self.q)
            f3 = Polynomial.random_polynomial(10, self.q)

            self.assertTrue(compare_polynomials(f1 + zero, f1))
            self.assertTrue(compare_polynomials(f1 + f2, f2 + f1))
            self.assertTrue(compare_polynomials(f1 + (f2 + f3), (f1 + f2) + f3))

            f2 = f1
            f2 += f1
            self.assertTrue(compare_polynomials(f1 + f1, f2))

    def test_sub_polynomials(self):
        for _ in range(10):
            f1 = Polynomial.random_polynomial(10, self.q)
            zero = Polynomial([0] * (len(f1.coefficients)), self.q)
            f2 = Polynomial.random_polynomial(10, self.q)
            f3 = Polynomial.random_polynomial(10, self.q)

            self.assertTrue(compare_polynomials(f1 - zero, f1))
            self.assertTrue(compare_polynomials(f3 - f3, zero))
            self.assertTrue(compare_polynomials(f3 - zero, f3))
            self.assertTrue(compare_polynomials(f1 - (f2 - f3), (f1 - f2) + f3))

            f2 = f1
            f2 -= f1
            self.assertTrue(compare_polynomials(f2, zero))

    def test_mul_polynomials(self):
        for _ in range(10):
            f1 = Polynomial.random_polynomial(10, self.q)
            zero = Polynomial([0], self.q)
            zeroCompare = Polynomial([0] * (len(f1.coefficients)), self.q)
            one = Polynomial([1], self.q)
            f2 = Polynomial.random_polynomial(10, self.q)
            f3 = Polynomial.random_polynomial(10, self.q)

            self.assertTrue(compare_polynomials(f1 * zero, zeroCompare))
            self.assertTrue(compare_polynomials(f1 * one, f1))
            self.assertTrue(compare_polynomials(f1 * f2, f2 * f1))
            self.assertTrue(compare_polynomials(f1 * (f2 * f3), (f1 * f2) * f3))

            f2 = f1
            f2 *= f2
            self.assertTrue(compare_polynomials(f1 * f1, f2))

    def test_mul_rq(self):
        for _ in range(10):
            f1 = Polynomial.random_polynomial(10, self.q)
            f2 = Polynomial.random_polynomial(10, self.q)
            n = 10
            result = f1.mulRq(f2, n)
            self.assertEqual(len(result.coefficients), n)

class TestPolynomialVector(unittest.TestCase):
    def setUp(self):
        self.q = 41

    def test_add_polynomial_vectors(self):
        for _ in range(10):
            v1 = PolynomialVector.random_polynomial_vector(5, 10, self.q)
            zero_vector = PolynomialVector([Polynomial([0], self.q) for _ in range(5)])
            v2 = PolynomialVector.random_polynomial_vector(5, 10, self.q)
            v3 = PolynomialVector.random_polynomial_vector(5, 10, self.q)

            self.assertTrue(compare_polynomial_vectors(v1 + zero_vector, v1))
            self.assertTrue(compare_polynomial_vectors(v1 + v2, v2 + v1))
            self.assertTrue(compare_polynomial_vectors(v1 + (v2 + v3), (v1 + v2) + v3))

            v2 = v1
            v2 += v1
            self.assertTrue(compare_polynomial_vectors(v1 + v1, v2))

    def test_sub_polynomial_vectors(self):
        for _ in range(10):
            v1 = PolynomialVector.random_polynomial_vector(5, 10, self.q)
            zero_vector = PolynomialVector([Polynomial([0] * len(v1.polynomials[0].coefficients), self.q) for _ in range(5)])
            v2 = PolynomialVector.random_polynomial_vector(5, 10, self.q)
            v3 = PolynomialVector.random_polynomial_vector(5, 10, self.q)
            
            self.assertTrue(compare_polynomial_vectors(v1 - zero_vector, v1))
            self.assertTrue(compare_polynomial_vectors(v3 - v3, zero_vector))
            self.assertTrue(compare_polynomial_vectors(v3 - zero_vector, v3))
            self.assertTrue(compare_polynomial_vectors(v1 - (v2 - v3), (v1 - v2) + v3))

            v2 = v1
            v2 -= v1
            self.assertTrue(compare_polynomial_vectors(v2, zero_vector))

if __name__ == '__main__':
    unittest.main()