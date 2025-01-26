from kyberPKE import generate_keypair, encrypt, decrypt, string_to_bitstring, bitstring_to_string
from kyber_params import KYBER_PARAMS

# Example usage:
params = KYBER_PARAMS["kyber512"]

public_key, private_key, t = generate_keypair(params)

# Convert the message to a bit string and pad it to the required length
message_str = "This is an encrypted message"
message_bits = string_to_bitstring(message_str)
message_bits_padded = message_bits.ljust(params["n"], '0')
message = [int(bit) for bit in message_bits_padded]

ciphertext, u, v = encrypt(params, public_key, message)

# Decrypt the message
decrypted_message_bits = decrypt(params, private_key, ciphertext)
decrypted_message_bits_str = ''.join(str(bit) for bit in decrypted_message_bits[:len(message_bits)])
decrypted_message = bitstring_to_string(decrypted_message_bits_str)

print("Original message:", message_str)
print("Decrypted message:", decrypted_message)