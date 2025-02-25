import unittest
from utils import (
    preprocessMessage, postprocessMessage, bytesToBitList, bitListToBytes,
    stringToBitstring, bitstringToString, decode, encode, compare_polynomials, compare_polynomial_vectors
)
from poly import Polynomial, PolynomialVector

class TestUtils(unittest.TestCase):
    def test_preprocess_message(self):
        message = "Hello"
        n = 40
        expected_bits = stringToBitstring(message).ljust(n, '0')
        expected = [int(bit) for bit in expected_bits]
        result = preprocessMessage(message, n)
        self.assertEqual(result, expected)

    def test_postprocess_message(self):
        message = "Hello"
        n = 40
        preprocessed = preprocessMessage(message, n)
        result = postprocessMessage(preprocessed, len(message) * 8)
        self.assertEqual(result, message)

    def test_bytes_to_bit_list(self):
        byte_data = b'\x01\x02'
        n = 16
        expected = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
        result = bytesToBitList(byte_data, n)
        self.assertEqual(result, expected)

    def test_bit_list_to_bytes(self):
        bit_list = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
        expected = b'\x01\x02'
        result = bitListToBytes(bit_list)
        self.assertEqual(result, expected)

    def test_string_to_bitstring(self):
        s = "A"
        expected = "01000001"
        result = stringToBitstring(s)
        self.assertEqual(result, expected)

    def test_bitstring_to_string(self):
        b = "01000001"
        expected = "A"
        result = bitstringToString(b)
        self.assertEqual(result, expected)

    def test_encode_decode_polynomial(self):
        poly = Polynomial([1, 2, 3, 4], 41)
        n = 4
        l = 6
        encoded = encode(poly, n, l)
        decoded = decode(encoded, 41, n, l)
        self.assertTrue(compare_polynomials(poly, decoded))

    def test_encode_decode_polynomial_vector(self):
        poly_vector = PolynomialVector([Polynomial([1, 2, 3, 4], 41), Polynomial([5, 6, 7, 8], 41)])
        n = 4
        l = 6
        k = 2
        encoded = encode(poly_vector, n, l)
        decoded = decode(encoded, 41, n, l, k)
        self.assertTrue(compare_polynomial_vectors(poly_vector, decoded))

    def test_compare_polynomials(self):
        p1 = Polynomial([1, 2, 3], 41)
        p2 = Polynomial([1, 2, 3], 41)
        p3 = Polynomial([1, 2, 4], 41)
        self.assertTrue(compare_polynomials(p1, p2))
        self.assertFalse(compare_polynomials(p1, p3))

    def test_compare_polynomial_vectors(self):
        v1 = PolynomialVector([Polynomial([1, 2, 3], 41), Polynomial([4, 5, 6], 41)])
        v2 = PolynomialVector([Polynomial([1, 2, 3], 41), Polynomial([4, 5, 6], 41)])
        v3 = PolynomialVector([Polynomial([1, 2, 3], 41), Polynomial([4, 5, 7], 41)])
        self.assertTrue(compare_polynomial_vectors(v1, v2))
        self.assertFalse(compare_polynomial_vectors(v1, v3))

if __name__ == '__main__':
    unittest.main()