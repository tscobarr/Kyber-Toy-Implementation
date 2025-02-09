import cProfile
from time import time
from kyber_params import KYBER_PARAMS
from kyberPKE import keygenPKE, encryptPKE, decryptPKE
from kyberKEM import keygenKEM, encapsulate, decapsulate

def profile_kyber_pke(params):
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

def profile_kyber_kem(params):
    ek, dk = keygenKEM(params)
    ciphertext, shared_secret = encapsulate(ek, params)

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

def benchmark_kyber_pke(params, name, count):
    keygen_times = []
    enc_times = []
    dec_times = []

    for _ in range(count):
        t0 = time()
        pk, sk = keygenPKE(params)
        keygen_times.append(time() - t0)

        message = [0] * params["n"]
        t1 = time()
        ciphertext = encryptPKE(params, pk, message)
        enc_times.append(time() - t1)

        t2 = time()
        _ = decryptPKE(params, sk, ciphertext)
        dec_times.append(time() - t2)

    avg_keygen = sum(keygen_times) / count
    avg_enc = sum(enc_times) / count
    avg_dec = sum(dec_times) / count
    print(
        f" {name:11} |"
        f"{avg_keygen*1000:7.2f}ms | {1/avg_keygen:10.2f} |"
        f"{avg_enc*1000:6.2f}ms | {1/avg_enc:9.2f} |"
        f"{avg_dec*1000:6.2f}ms | {1/avg_dec:7.2f} |"
    )

def benchmark_kyber_kem(params, name, count):
    keygen_times = []
    enc_times = []
    dec_times = []

    for _ in range(count):
        t0 = time()
        ek, dk = keygenKEM(params)
        keygen_times.append(time() - t0)

        t1 = time()
        ciphertext, shared_secret = encapsulate(ek, params)
        enc_times.append(time() - t1)

        t2 = time()
        _ = decapsulate(dk, ciphertext, params)
        dec_times.append(time() - t2)

    avg_keygen = sum(keygen_times) / count
    avg_enc = sum(enc_times) / count
    avg_dec = sum(dec_times) / count
    print(
        f" {name:11} |"
        f"{avg_keygen*1000:7.2f}ms | {1/avg_keygen:10.2f} |"
        f"{avg_enc*1000:6.2f}ms | {1/avg_enc:9.2f} |"
        f"{avg_dec*1000:6.2f}ms | {1/avg_dec:7.2f} |"
    )

if __name__ == "__main__":
    count = 1000
    params_kyber512 = KYBER_PARAMS["kyber512"]
    params_kyber768 = KYBER_PARAMS["kyber768"]
    params_kyber1024 = KYBER_PARAMS["kyber1024"]

    # common banner
    print("-" * 80)
    print(
        "   Params    |  keygen  |  keygen/s  |  enc  |  enc/s  "
        "|  dec  |  dec/s"
    )
    print("-" * 80)

    # Benchmark Kyber-PKE
    benchmark_kyber_pke(params_kyber512, "Kyber512 PKE", count)
    benchmark_kyber_pke(params_kyber768, "Kyber768 PKE", count)
    benchmark_kyber_pke(params_kyber1024, "Kyber1024 PKE", count)

    # Benchmark Kyber-KEM
    benchmark_kyber_kem(params_kyber512, "Kyber512 KEM", count)
    benchmark_kyber_kem(params_kyber768, "Kyber768 KEM", count)
    benchmark_kyber_kem(params_kyber1024, "Kyber1024 KEM", count)