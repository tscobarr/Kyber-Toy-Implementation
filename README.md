# Kyber PKE Toy Implementation

This repository contains a toy implementation of the Kyber Public Key Encryption (PKE) scheme. This implementation is intended for educational purposes only and should not be used for any other purpose.

## Overview

Kyber is a lattice-based cryptographic algorithm that provides secure public key encryption. This implementation is based on one of the first versions of Kyber PKE. We are planning on improving it by adding some optimizations and making Kyber Key Encapsulation Mechanism (KEM).

## Files

- `kyberPKE.py`: Contains the core functions for key generation, encryption, and decryption.
- `poly.py`: Defines the `Polynomial` class and its operations.
- `vector.py`: Defines the `PolynomialVector` class and its operations.
- `norms.py`: Contains utility functions for computing norms and rounding.
- `kyber_params.py`: Defines the parameters for different versions of Kyber (Kyber512, Kyber768, Kyber1024).
- `main.py`: Example usage of the Kyber PKE implementation.
- `test.py`: Unit tests for the `Polynomial`, `PolynomialVector`, and utility functions.

## Usage

Can see an example in main

## Disclaimer

This is a toy implementation of the Kyber PKE scheme and is intended for educational purposes only. It should not be used for any other purpose. The implementation may lack optimizations and security features present in production-ready cryptographic libraries.

## Future Work
We are planning on improving this implementation by adding some optimizations and making Kyber Key Encapsulation Mechanism (KEM).