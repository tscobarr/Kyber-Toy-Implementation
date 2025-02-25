import unittest
from optimization import (
    roundUpTies, mods, roundQ, H, G, XOF, PRF, KDF, cbd, randomPolyVector, randomPoly, expand, compress, decompress
)
from poly import Polynomial, PolynomialVector

class TestOptimization(unittest.TestCase):
    def test_round_up_ties(self):
        self.assertEqual(roundUpTies(2.5), 3)
        self.assertEqual(roundUpTies(-3.5), -3)
        self.assertEqual(roundUpTies(2.4), 2)
        self.assertEqual(roundUpTies(2.6), 3)

    def test_mods(self):
        self.assertEqual(mods(5, 3), -1)
        self.assertEqual(mods(-5, 3), 1)
        self.assertEqual(mods(4, 3), 1)
        self.assertEqual(mods(-4, 3), -1)

    def test_round_q(self):
        self.assertEqual(roundQ(5, 16), 1)
        self.assertEqual(roundQ(3, 16), 0)
        self.assertEqual(roundQ(-5, 16), 1)
        self.assertEqual(roundQ(-3, 16), 0)

    def test_hash_functions(self):
        data = b"test"
        self.assertEqual(len(H(data)), 32)
        self.assertEqual(len(G(data)), 64)
        self.assertEqual(len(XOF(data, 16)), 16)

    def test_prf(self):
        seed = b"seed"
        nonce = 1
        length = 32
        self.assertEqual(len(PRF(seed, nonce, length)), length)

    def test_kdf(self):
        data = b"data"
        length = 32
        self.assertEqual(len(KDF(data, length)), length)

    def test_cbd(self):
        eta = 3
        inputBytes = b'\x00' * (64 * eta)
        coefficients = cbd(inputBytes, eta)
        self.assertEqual(len(coefficients), 256)

    def test_random_poly_vector(self):
        k = 2
        N = 0
        q = 3329
        eta = 3
        seed = b"seed"
        poly_vector = randomPolyVector(k, N, q, eta, seed)
        self.assertEqual(len(poly_vector.polynomials), k)
        self.assertEqual(len(poly_vector.polynomials[0].coefficients), 256)

    def test_random_poly(self):
        q = 3329
        eta = 3
        seed = b"seed"
        N = 0
        poly = randomPoly(q, eta, seed, N)
        self.assertEqual(len(poly.coefficients), 256)

    def test_expand(self):
        rho = b"rho"
        k = 2
        q = 3329
        n = 256
        matrix = expand(rho, k, q, n)
        self.assertEqual(len(matrix), k)
        self.assertEqual(len(matrix[0]), k)
        self.assertEqual(len(matrix[0][0].coefficients), n)

    def test_compress_decompress(self):
        x = 1234
        q = 3
        d = 10
        compressed = compress(x, q, d)
        decompressed = decompress(compressed, q, d)
        self.assertEqual(decompressed, x % q)

if __name__ == '__main__':
    unittest.main()