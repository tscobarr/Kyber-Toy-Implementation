import cProfile
from time import time
from params import KYBER_PARAMS
from kyberPKE import keygenPKE, encryptPKE, decryptPKE
from kyberKEM import keygenKEM, encapsulate, decapsulate

def profileKyberPKE(params):
    pk, sk = keygenPKE(params)
    message = [0] * params["n"]
    ciphertext = encryptPKE(params, pk, message)

    gvars = {}
    lvars = {"params": params, "pk": pk, "sk": sk, "message": message, "ciphertext": ciphertext}

    cProfile.runctx(
        "[keygenPKE(params) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )
    cProfile.runctx(
        "[encryptPKE(params, pk, message) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )
    cProfile.runctx(
        "[decryptPKE(params, sk, ciphertext) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )

def profileKyberKEM(params):
    ek, dk = keygenKEM(params)
    ciphertext, sharedSecret = encapsulate(ek, params)

    gvars = {}
    lvars = {"params": params, "ek": ek, "dk": dk, "ciphertext": ciphertext}

    cProfile.runctx(
        "[keygenKEM(params) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )
    cProfile.runctx(
        "[encapsulate(ek, params) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )
    cProfile.runctx(
        "[decapsulate(dk, ciphertext, params) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )

def benchmarkKyberPKE(params, name, count):
    keygenTimes = []
    encTimes = []
    decTimes = []

    for _ in range(count):
        t0 = time()
        pk, sk = keygenPKE(params)
        keygenTimes.append(time() - t0)

        message = [0] * params["n"]
        t1 = time()
        ciphertext = encryptPKE(params, pk, message)
        encTimes.append(time() - t1)

        t2 = time()
        _ = decryptPKE(params, sk, ciphertext)
        decTimes.append(time() - t2)

    avgKeygen = sum(keygenTimes) / count
    avgEnc = sum(encTimes) / count
    avgDec = sum(decTimes) / count
    print(
        f" {name:11} |"
        f"{avgKeygen*1000:7.2f}ms | {1/avgKeygen:10.2f} |"
        f"{avgEnc*1000:6.2f}ms | {1/avgEnc:9.2f} |"
        f"{avgDec*1000:6.2f}ms | {1/avgDec:7.2f} |"
    )

def benchmarkKyberKEM(params, name, count):
    keygenTimes = []
    encTimes = []
    decTimes = []

    for _ in range(count):
        t0 = time()
        ek, dk = keygenKEM(params)
        keygenTimes.append(time() - t0)

        t1 = time()
        ciphertext, sharedSecret = encapsulate(ek, params)
        encTimes.append(time() - t1)

        t2 = time()
        _ = decapsulate(dk, ciphertext, params)
        decTimes.append(time() - t2)

    avgKeygen = sum(keygenTimes) / count
    avgEnc = sum(encTimes) / count
    avgDec = sum(decTimes) / count
    print(
        f" {name:11} |"
        f"{avgKeygen*1000:7.2f}ms | {1/avgKeygen:10.2f} |"
        f"{avgEnc*1000:6.2f}ms | {1/avgEnc:9.2f} |"
        f"{avgDec*1000:6.2f}ms | {1/avgDec:7.2f} |"
    )

if __name__ == "__main__":
    count = 1000
    paramsKyber512 = KYBER_PARAMS["kyber512"]
    paramsKyber768 = KYBER_PARAMS["kyber768"]
    paramsKyber1024 = KYBER_PARAMS["kyber1024"]

    # common banner
    print("-" * 80)
    print(
        "   Params    |  keygen  |  keygen/s  |  enc  |  enc/s  "
        "|  dec  |  dec/s"
    )
    print("-" * 80)

    # Benchmark Kyber-PKE
    benchmarkKyberPKE(paramsKyber512, "Kyber512 PKE", count)
    benchmarkKyberPKE(paramsKyber768, "Kyber768 PKE", count)
    benchmarkKyberPKE(paramsKyber1024, "Kyber1024 PKE", count)

    # Benchmark Kyber-KEM
    benchmarkKyberKEM(paramsKyber512, "Kyber512 KEM", count)
    benchmarkKyberKEM(paramsKyber768, "Kyber768 KEM", count)
    benchmarkKyberKEM(paramsKyber1024, "Kyber1024 KEM", count)