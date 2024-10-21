import time
import matplotlib.pyplot as plt
from Crypto.Cipher import DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# Encrypt/Decrypt function that handles everything
# Copied directly from PyCryptodome Documentation
def process_data(plaintext, key, mode='encrypt', algorithm='DES'):
    if algorithm == 'DES':
        cipher = DES.new(key, DES.MODE_ECB)
        block_size = DES.block_size
    else:
        cipher = DES3.new(key, DES3.MODE_ECB)
        block_size = DES3.block_size

    if mode == 'encrypt':
        padded_text = pad(plaintext.encode(), block_size)
        return cipher.encrypt(padded_text)
    else:
        return unpad(cipher.decrypt(plaintext), block_size).decode()


#
def week_4():
    timings = {}

    # Read plaintext from file, change the path for your own file
    with open("test.txt", 'r') as file:
        plaintext = file.read()

    #increaing the size of the text file
    iterations = 100
    plaintext *= iterations

    print(f"plaintext size: {len(plaintext)} characters\n")

    # DES encryption and decryption
    des_key = get_random_bytes(8)  # 64-bit key for DES, You should use get_random_bytes instead of random (the module)
    # random isn't cryptographically secure and shouldn't be used for DES's Key gen or IVs

    start = time.perf_counter()
    for _ in range(iterations):
        des_encrypted = process_data(plaintext, des_key, mode='encrypt', algorithm='DES')
    timings['DES Encryption'] = (time.perf_counter() - start)
    print(f"DES encrypted: {des_encrypted[:32]}...")  # Show head of the encrypted text

    start = time.perf_counter()
    for _ in range(iterations):
        des_decrypted = process_data(des_encrypted, des_key, mode='decrypt', algorithm='DES')
    timings['DES Decryption'] = (time.perf_counter() - start)
    print(f"DES decrypted: {des_decrypted[:32]}...")  # Show head of the decrypted text

    # 3DES encryption and decryption
    des3_key = DES3.adjust_key_parity(get_random_bytes(24))  # 192-bit key for 3DES
    start = time.perf_counter()
    for _ in range(iterations):
        des3_encrypted = process_data(plaintext, des3_key, mode='encrypt', algorithm='DES3')
    timings['3DES Encryption'] = (time.perf_counter() - start)
    print(f"3DES encrypted: {des3_encrypted[:32]}...")  # Show head of the encrypted text

    start = time.perf_counter()
    for _ in range(iterations):
        des3_decrypted = process_data(des3_encrypted, des3_key, mode='decrypt', algorithm='DES3')
    timings['3DES Decryption'] = (time.perf_counter() - start)
    print(f"3DES decrypted: {des3_decrypted[:32]}...")  # Show head of the decrypted text

    return timings


# function to Plot timings in a chart
def plot_timings(timings):
    operations = list(timings.keys())
    times = list(timings.values())

    x = range(len(operations))
    # Sub-plots to style the charts for better reading
    fig, ax = plt.subplots()

    # DES bars
    ax.bar(x[0], times[0], width=0.4, label='DES Encryption', color='blue')
    ax.bar(x[1], times[1], width=0.4, label='DES Decryption', color='green')

    # 3DES bars
    ax.bar(x[2], times[2], width=0.4, label='3DES Encryption', color='orange', hatch='//')
    ax.bar(x[3], times[3], width=0.4, label='3DES Decryption', color='red', hatch='//')

    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['DES Encryption', 'DES Decryption', '3DES Encryption', '3DES Decryption'])

    ax.set_xlabel('Operation')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('DES and 3DES Encryption/Decryption Times')
    #ax.set_yscale('log') # optional code to display the time in log scale

    # Add legend
    ax.legend(draggable=True)

    plt.show()

# Main execution
timings = week_4()
#print(timings)
plot_timings(timings)
