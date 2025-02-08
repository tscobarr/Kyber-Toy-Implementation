from kyber_params import KYBER_PARAMS
from kyberPKE import keygenPKE, encrypt, decrypt, encryptPKE, decryptPKE
from kyberKEM import keygenKEM, encapsulate, decapsulate
from utils import bitstring_to_string, string_to_bitstring, preprocess_message, postprocess_message

def main():
    # Example usage for Kyber-PKE
    params = KYBER_PARAMS["kyber512"]

    print("Testing Kyber-PKE:")

    # Generate PKE keypair
    public_key, private_key = keygenPKE(params)

    # Encrypt the message
    message_str = "This is an encrypted message"
    ciphertext = encrypt(params, public_key, message_str)

    # Decrypt the message
    decrypted_message = decrypt(params, private_key, ciphertext)

    print("Original message:", message_str)
    print("Decrypted message:", decrypted_message)

    # Example usage for Kyber-KEM
    print("\nTesting Kyber-KEM:")
    
    # Generate KEM keypair
    ek, dk = keygenKEM(params)

    # Encapsulate|
    ciphertext_kem, shared_secret_enc = encapsulate(ek, params, dk)

    # Decapsulate
    shared_secret_dec = decapsulate(dk, ciphertext_kem, params)

    # Verify if the shared secrets match
    if shared_secret_enc == shared_secret_dec:
        print("KEM test passed: Shared secrets match.")
    else:
        print("KEM test failed: Shared secrets do not match.")

if __name__ == "__main__":
    main()