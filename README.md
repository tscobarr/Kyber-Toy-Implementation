# Kyber Toy Implementation

This repository contains a toy implementation of the Kyber Public Key Encryption (PKE) scheme and Key Encapsulation Mechanism (KEM) . This implementation is intended for educational purposes only.

## Overview

Kyber is a lattice-based cryptographic algorithm that provides secure public key encryption and key encapsulation. This implementation is not the complete version of kyber, but have some optimization.

## Usage

### Define params (512, 768 or 1024)

```python
params = KYBER_PARAMS["kyber512"]
```

### Kyber PKE

```python
publicKey, privateKey = keygenPKE(params)
messageStr = "This is an encrypted message"
cipherText = encrypt(params, publicKey, messageStr)
decryptedMessage = decrypt(params, privateKey, cipherText)
```

### Kyber KEM

```python
pk, sk = keygenKEM(params)
cipherTextKem, sharedSecretEnc = encapsulate(pk, params)
sharedSecretDec = decapsulate(cipherTextKem, sk, params)
```

## Benchmarks

|     Params    |  keygen  |  keygen/s  |   enc   |   enc/s   |   dec   |  dec/s  |
|---------------|---------:|-----------:|--------:|----------:|--------:|--------:|
| Kyber512 PKE  |  35.64ms |      28.06 | 52.67ms |     18.99 | 17.62ms |   56.74 |
| Kyber768 PKE  |  77.73ms |      12.87 |102.84ms |      9.72 | 26.38ms |   37.91 |
| Kyber1024 PKE | 135.18ms |       7.40 |168.91ms |      5.92 | 35.23ms |   28.38 |
| Kyber512 KEM  |  35.34ms |      28.29 | 52.43ms |     19.07 | 67.20ms |   14.88 |
| Kyber768 KEM  |  76.78ms |      13.03 |102.20ms |      9.79 |123.90ms |    8.07 |
| Kyber1024 KEM | 138.66ms |       7.21 |173.32ms |      5.77 |203.92ms |    4.90 |

 All times recorded using a Ryzen 5 5600x CPU and averaged over 1000 runs.

## Disclaimer

This is a toy implementation and is intended for educational purposes only. It should not be used for any other purpose. The implementation may lack optimizations and security features present in production-ready cryptographic libraries.

## Future Work
We are planning on improving this implementation by adding some more optimizations like NTT and fixing some other security problems like constant time.