import unittest
from kyberKEM import keygenKEM, encapsulate, decapsulate

class TestKyberKEM(unittest.TestCase):
    def setUp(self):
        self.params = {
            "k": 2,
            "n": 256,
            "q": 3329,
            "eta1": 3,
            "eta2": 2,
            "du": 10,
            "dv": 4
        }

    def test_keygenKEM(self):
        pk, sk = keygenKEM(self.params)
        sk0Len = 12 * self.params["k"] * 256 // 8
        pkLen = sk0Len + 32
        hLen = 32
        zLen = 32
        expected_sk_len = sk0Len + pkLen + hLen + zLen
        self.assertEqual(len(pk), 32 + self.params["k"] * self.params["n"] * 12 // 8)
        self.assertEqual(len(sk), expected_sk_len)

    def test_encapsulate_decapsulate(self):
        pk, sk = keygenKEM(self.params)
        ciphertext, shared_secret_enc = encapsulate(pk, self.params)
        shared_secret_dec = decapsulate(ciphertext, sk, self.params)
        self.assertEqual(shared_secret_enc, shared_secret_dec)

if __name__ == '__main__':
    unittest.main()