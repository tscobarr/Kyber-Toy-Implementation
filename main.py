from kyberParams import KYBER_PARAMS
from kyberPKE import keygenPKE, encrypt, decrypt
from kyberKEM import keygenKEM, encapsulate, decapsulate

def main():
    # Example usage for Kyber-PKE
    params = KYBER_PARAMS["kyber1024"]

    print("Testing Kyber-PKE:")

    # Generate PKE keypair
    publicKey, privateKey = keygenPKE(params)

    # Encrypt the message
    messageStr = "This is an encrypted message"
    cipherText = encrypt(params, publicKey, messageStr)

    # Decrypt the message
    decryptedMessage = decrypt(params, privateKey, cipherText)

    print("Original message:", messageStr)
    print("Decrypted message:", decryptedMessage)

    # Example usage for Kyber-KEM
    print("\nTesting Kyber-KEM:")
    
    # Generate KEM keypair
    pk, sk = keygenKEM(params)

    # Encapsulate
    cipherTextKem, sharedSecretEnc = encapsulate(pk, params)

    # Decapsulate
    sharedSecretDec = decapsulate(cipherTextKem, sk, params)

    # Verify if the shared secrets match
    if sharedSecretEnc == sharedSecretDec:
        print("KEM test passed: Shared secrets match.")
    else:
        print("KEM test failed: Shared secrets do not match.")

if __name__ == "__main__":
    main()