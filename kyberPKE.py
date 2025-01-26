import secrets
import math
from poly import Polynomial
from vector import PolynomialVector
from norms import infinity_norm_polynomial, round_q
from kyber_params import KYBER_PARAMS

def round_up_ties(x):
    """
    Returns the closest integer to x, breaking ties upwards.

    Parameters:
        x (float): The input number.

    Returns:
        int: The rounded integer.
    """
    if x - math.floor(x) == 0.5:  # Check for ties (e.g., 2.5, -3.5)
        return math.ceil(x)
    return round(x)

def generate_random_polynomial_vector(k, n, q, eta):
    polynomials = []
    for _ in range(k):
        while True:
            coefficients = [secrets.randbelow(2 * eta + 1) - eta for _ in range(n)]
            poly = Polynomial(coefficients, q)
            if infinity_norm_polynomial(poly) <= eta:
                polynomials.append(poly)
                break
    return PolynomialVector(polynomials)

def generate_keypair(params):
    k = params["k"]
    n = params["n"]
    q = params["q"]
    eta1 = params["eta1"]
    eta2 = params["eta2"]

    # Step 1: Select A ∈_R (R_q)^k*k, s ∈_R (S_eta1)^k', and e ∈_R (S_eta2)^k
    A = [[Polynomial([secrets.randbelow(q) for _ in range(n)], q) for _ in range(k)] for _ in range(k)]
    s = generate_random_polynomial_vector(k, n, q, eta1)
    e = generate_random_polynomial_vector(k, n, q, eta2)

    # Step 2: Compute As
    As = PolynomialVector([Polynomial([0] * n, q) for _ in range(k)])
    for i in range(k):
        for j in range(k):
            As.polynomials[i] = As.polynomials[i] + A[i][j].mul_rq(s.polynomials[j], n)

    # Compute t = As + e
    t = PolynomialVector([As.polynomials[i] + e.polynomials[i] for i in range(k)])

    # Step 3: Alice's encryption (public) key is (A, t); her decryption (private) key is s
    public_key = (A, t)
    private_key = s

    return public_key, private_key, t

def encrypt(params, public_key, message):
    k = params["k"]
    n = params["n"]
    q = params["q"]
    eta1 = params["eta1"]
    eta2 = params["eta2"]

    A, t = public_key

    # Step 2: Select r ∈_R (S_eta1)^k, e_1 ∈_R (S_eta2)^k, e_2 ∈_R S_eta2
    r = generate_random_polynomial_vector(k, n, q, eta1)
    e1 = generate_random_polynomial_vector(k, n, q, eta2)
    e2 = Polynomial([secrets.randbelow(2 * eta2 + 1) - eta2 for _ in range(n)], q)

    # Step 3: Compute u = A^T*r + e_1
    u = PolynomialVector([Polynomial([0] * n, q) for _ in range(k)])
    for i in range(k):
        for j in range(k):
            u.polynomials[i] = u.polynomials[i] + A[j][i].mul_rq(r.polynomials[j], n)
        u.polynomials[i] = u.polynomials[i] + e1.polynomials[i]

    # Step 4: Compute v = t^T*r + e_2 + ⌈q/2⌋*m
    v = Polynomial([0] * n, q)
    for i in range(k):
        v = v + t.polynomials[i].mul_rq(r.polynomials[i], n)
    v = v + e2

    # Add ⌈q/2⌋*m to v
    q_half = round_up_ties(q / 2)
    m_poly = Polynomial([m * q_half for m in message], q)
    v = v + m_poly

    # Output c = (u, v)
    ciphertext = (u, v)
    return ciphertext, u, v

def decrypt(params, private_key, ciphertext):
    k = params["k"]
    n = params["n"]
    q = params["q"]

    s = private_key
    u, v = ciphertext

    # Step 1: Compute m = Round_q(v - s^T * u)
    s_u = Polynomial([0] * n, q)
    for i in range(k):
        s_u = s_u + s.polynomials[i].mul_rq(u.polynomials[i], n)
    m_poly = v - s_u
    message = [round_q(c, q) for c in m_poly.coefficients]

    return message

def string_to_bitstring(s):
    return ''.join(format(ord(c), '08b') for c in s)

def bitstring_to_string(b):
    chars = [chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8)]
    return ''.join(chars)