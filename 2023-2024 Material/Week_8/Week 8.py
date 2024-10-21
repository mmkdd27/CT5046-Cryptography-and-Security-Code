import time
import hashlib

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Separate function to time the Hashing process
def hash_data(data):
    timings = {}

    start = time.perf_counter()
    md5_hash = hashlib.md5(data).hexdigest()
    timings['MD5 Hashing'] = time.perf_counter() - start
    print(f"MD5: {md5_hash}")
    # SHA-256 hashing
    start = time.perf_counter()
    sha256_hash = hashlib.sha256(data).hexdigest()
    timings['SHA-256 Hashing'] = time.perf_counter() - start
    print(f"SHA-256: {sha256_hash}")

    return timings


# Encrypt/Decrypt function that handles everything
# Copied directly from PyCryptodome Documentation
def process_data(plaintext, key, mode='encrypt', algorithm='DES'):
    cipher = DES.new(key, DES.MODE_ECB)
    block_size = DES.block_size

    if mode == 'encrypt':
        padded_text = pad(plaintext.encode(), block_size)
        return cipher.encrypt(padded_text)
    else:
        return unpad(cipher.decrypt(plaintext), block_size).decode()



def week_8():
    # Read plaintext from file, change the path for your own file
    with open("test.txt", 'r') as file:
        plaintext = file.read()

    print(f"Plaintext size: {len(plaintext)} characters\n")

    des_key = get_random_bytes(8)
    encrypted_data = process_data(plaintext, des_key)

    timings = hash_data(encrypted_data)

    # Print timings
    print(f"MD5 Hashing Time: {timings['MD5 Hashing']} seconds")
    print(f"SHA-256 Hashing Time: {timings['SHA-256 Hashing']} seconds")


week_8()
