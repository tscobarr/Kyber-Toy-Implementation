# Kyber Toy Implementation

This repository contains a toy implementation of the Kyber Public Key Encryption (PKE) scheme and Key Encapsulation Mechanism (KEM) . This implementation is intended for educational purposes only.

## Overview

Kyber is a lattice-based cryptographic algorithm that provides secure public key encryption and key encapsulation. This implementation is not the complete version of kyber, but have some optimization.

## Usage

Can see example in main.

## Benchmarks

|   Params      |  keygen  |  keygen/s  |   enc   |   enc/s   |   dec   |  dec/s
|---------------|----------|------------|---------|-----------|---------|--------
| Kyber512 PKE  |  34.32ms |      29.14 | 52.45ms |     19.06 | 16.40ms |   60.96 |
| Kyber768 PKE  |  75.70ms |      13.21 |102.24ms |      9.78 | 24.47ms |   40.87 |
| Kyber1024 PKE | 133.86ms |       7.47 |169.17ms |      5.91 | 32.53ms |   30.74 |
| Kyber512 KEM  |  34.80ms |      28.74 | 52.87ms |     18.92 | 69.04ms |   14.48 |
| Kyber768 KEM  |  76.09ms |      13.14 |102.71ms |      9.74 |126.72ms |    7.89 |
| Kyber1024 KEM | 133.81ms |       7.47 |169.11ms |      5.91 |200.86ms |    4.98 |

 All times recorded using a Ryzen 5 5600x CPU and averaged over 1000 runs.

## Disclaimer

This is a toy implementation and is intended for educational purposes only. It should not be used for any other purpose. The implementation may lack optimizations and security features present in production-ready cryptographic libraries.

## Future Work
We are planning on improving this implementation by adding some more optimizations like NTT and fixing some other security problems.