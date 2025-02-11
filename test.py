from utils import encode, decode

def checkLenght(byteArray, l):
    """Checks if the byte array is of the correct size (32 * l bytes).

    Args:
        byteArray (bytes): The input byte array.
        l (int): The length parameter.

    Returns:
        bool: True if the byte array is of the correct size, False otherwise.
    """
    return len(byteArray) == 32 * l

from kyberPKE import keygenPKE

# Define parameters
params = {
    "k": 2,
    "n": 256,
    "q": 3329,
    "eta1": 3,
    "eta2": 3
}

# Generate key pair
publicKey, privateKey = keygenPKE(params)

# Extract rho and t from the public key
rho = publicKey[:32]
serializedT = publicKey[32:]
t = decode(serializedT, params["q"], params["n"], 12, params["k"])

# Encode and decode each polynomial in the public key
for poly in t.polynomials:
    # Encode the polynomial to bytes
    encodedBytes = encode(poly, params["n"], 12)
    
    # Check the length of the encoded bytes
    assert checkLenght(encodedBytes, 12), "Encoded public key polynomial length is incorrect"
    
    # Decode the bytes back to a polynomial
    decodedPoly = decode(encodedBytes, params["q"], params["n"], 12)
    
    # Compare the original and decoded polynomials
    for i, (originalCoeff, decodedCoeff) in enumerate(zip(poly.coefficients, decodedPoly.coefficients)):
        if originalCoeff != decodedCoeff:
            print(f"Mismatch at coefficient {i} in public key polynomial")
            print(f"Original coefficient: {originalCoeff}")
            print(f"Decoded coefficient: {decodedCoeff}")
        assert originalCoeff == decodedCoeff, f"Mismatch at coefficient {i} in public key polynomial"

print("All polynomials in the public key were successfully encoded and decoded.")

# Decode the private key
s = decode(privateKey, params["q"], params["n"], 12, params["k"])

# Encode and decode each polynomial in the private key
for poly in s.polynomials:
    # Encode the polynomial to bytes
    encodedBytes = encode(poly, params["n"], 12)
    
    # Check the length of the encoded bytes
    assert checkLenght(encodedBytes, 12), "Encoded private key polynomial length is incorrect"
    
    # Decode the bytes back to a polynomial
    decodedPoly = decode(encodedBytes, params["q"], params["n"], 12)
    
    # Compare the original and decoded polynomials
    for i, (originalCoeff, decodedCoeff) in enumerate(zip(poly.coefficients, decodedPoly.coefficients)):
        if originalCoeff != decodedCoeff:
            print(f"Mismatch at coefficient {i} in private key polynomial")
            print(f"Original coefficient: {originalCoeff}")
            print(f"Decoded coefficient: {decodedCoeff}")
        assert originalCoeff == decodedCoeff, f"Mismatch at coefficient {i} in private key polynomial"

print("All polynomials in the private key were successfully encoded and decoded.")