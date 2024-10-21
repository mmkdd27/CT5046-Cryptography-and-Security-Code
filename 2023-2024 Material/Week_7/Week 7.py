import timeit
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

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


def week_7():
    timings = {}

    # Read plaintext from file, change the path for your own file
    with open("test.txt", 'r') as file:
        plaintext = file.read()

    # Increasing the size of the text file
    iterations = 100
    plaintext *= iterations

    print(f"plaintext size: {len(plaintext)} characters\n")

    # DES encryption and decryption
    des_key = get_random_bytes(8)  # 64-bit key for DES
    start = timeit.timeit()
    for _ in range(iterations):
        des_encrypted = process_data(plaintext, des_key, mode='encrypt', algorithm='DES')
    timings['DES Encryption'] = (timeit.timeit() - start)
    print(f"DES encrypted: {des_encrypted[:32]}...")  # Show head of the encrypted text

    start = timeit.timeit()
    for _ in range(iterations):
        des_decrypted = process_data(des_encrypted, des_key, mode='decrypt', algorithm='DES')
    timings['DES Decryption'] = (timeit.timeit() - start)
    print(f"DES decrypted: {des_decrypted[:32]}...")  # Show head of the decrypted text

    # Print timings
    print(f"DES Encryption Time: {timings['DES Encryption']} seconds")
    print(f"DES Decryption Time: {timings['DES Decryption']} seconds")


# Main execution
week_7()
