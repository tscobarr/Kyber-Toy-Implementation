import unittest
from kyberPKE import keygenPKE, encrypt, decrypt
from utils import preprocessMessage, postprocessMessage

class TestKyberPKE(unittest.TestCase):
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

    def test_keygenPKE(self):
        publicKey, privateKey = keygenPKE(self.params)
        self.assertEqual(len(publicKey), 32 + self.params["k"] * self.params["n"] * 12 // 8)
        self.assertEqual(len(privateKey), self.params["k"] * self.params["n"] * 12 // 8)

    def test_encrypt_decrypt(self):
        publicKey, privateKey = keygenPKE(self.params)
        message = "Hello, Kyber"
        ciphertext = encrypt(self.params, publicKey, message)
        decryptedMessage = decrypt(self.params, privateKey, ciphertext)
        # Remove trailing null characters from the decrypted message
        decryptedMessage = decryptedMessage.rstrip('\x00')
        self.assertEqual(decryptedMessage, message)

if __name__ == '__main__':
    unittest.main()