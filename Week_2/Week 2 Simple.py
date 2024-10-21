import numpy as np
from rich import print
from pycipher import Playfair
from tensorflow.python.ops.logging_ops import Print


# Not my code
def mod_inverse(a, m):
    # Finds the modular inverse of a under modulo m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
# Not my code

def hill_cipher_encrypt(plaintext, key_matrix):
    # Hill cipher implementation using NumPy array functionality
    # since Hill cipher isn't in the Pychipher module
    plaintext = plaintext.upper().replace(" ", "")
    # preformatting the plaintext
    # if the scope of the module would have allowed I would carry the capitalization as a binary bitmask
    # and attach an encoded version as a tail to the plaintext
    # if you are another student reading this I would encourage you to implement this

    matrix_size = len(key_matrix)
    if len(plaintext) % matrix_size != 0:
        # Pad the plaintext with 'X' if it fit into the matrix
        plaintext += 'X' * (matrix_size - len(plaintext) % matrix_size)

    # Convert plaintext to numbers
    plaintext_numbers = [ord(char) - 65 for char in plaintext]

    # Encryption
    ciphertext_numbers = []
    for i in range(0, len(plaintext_numbers), matrix_size): # Reads through the plaintext in blocks the length of the matrix
        block = np.array(plaintext_numbers[i:i + matrix_size]) # creates a NumPy array the same size as the lenght of the matrix
        cipher_block = np.dot(key_matrix, block) % 26 # dot product ot scalar product, this takes the two matrix's and returns an int,
        # it's reduced with the % opreator to keep it withing the english alphabet,
        # if you aren't turning it into a letter again for the ciphertext you could just keep it as a int > 26
        ciphertext_numbers.extend(cipher_block)

    # Convert numbers back to letters
    ciphertext = ''.join(chr(num + 65) for num in ciphertext_numbers)
    return ciphertext


def hill_cipher_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace(" ", "")
    matrix_size = len(key_matrix)

    # Find the determinant of the key matrix and its modular inverse
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26
    print(f"Determinant: {determinant}")  # Debugging line to see the determinant
    inv_determinant = mod_inverse(determinant, 26)

    if inv_determinant is None:
        raise ValueError("Matrix determinant is not invertible under mod 26")
        Print("if you are facing this error i would recommend looking online for a valid hill cipher key square, I usually use:")
        print(" 1 2 ")
        print(" 3 5 ")
    # Find the inverse of the key matrix
    adjugate_matrix = np.round(inv_determinant * np.linalg.det(key_matrix) * np.linalg.inv(key_matrix)).astype(int) % 26

    # Convert ciphertext to numbers
    ciphertext_numbers = [ord(char) - 65 for char in ciphertext]

    # Decryption
    plaintext_numbers = []
    for i in range(0, len(ciphertext_numbers), matrix_size):
        block = np.array(ciphertext_numbers[i:i + matrix_size])
        plain_block = np.dot(adjugate_matrix, block) % 26
        plaintext_numbers.extend(plain_block)

    # Convert numbers back to letters
    plaintext = ''.join(chr(num + 65) for num in plaintext_numbers)
    return plaintext

def week_2():
    print("Task:")
    print("Create a CryptTool project which accepts plaintext and")
    print("◙ First encrypts it using [green]Hill Cipher[/green]")
    print("◙ Then encrypts the Hill Cipher with [green]Playfair Cipher[/green]")
    print("◙ Then decrypts it back to the original plaintext")
    print(
        "\nInput(Plaintext) -> encrypt with [green]Hill cipher[/green] -> encrypt with [green]Playfair cipher[/green] -> decrypt Playfair cipher -> decrypt [green]Hill cipher -> Output(plaintext)")

    # Error Handling
    while True:
        try:
            print("Please enter the Matrix size for Hill cipher (2<n):")
            matrix_size = int(input())
            if matrix_size < 2:
                raise ValueError("Matrix size must be greater than 1.")
            break
        except ValueError as e:
            print(f"[red]Error: {e}. Try again![/red]")

    # Hill cipher key matrix
    print(f"Enter {matrix_size}x{matrix_size} matrix for Hill Cipher key:")
    key_matrix = []
    for i in range(matrix_size):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated numbers): ").split()))
        key_matrix.append(row)
    key_matrix = np.array(key_matrix)

    #print("Please enter the keyword for the [green] Playfair cipher[/green]:")
    #keyword = input()
    # TODO: Genrate Keysqure from user input

    plaintext = input("Enter input text: ")
    print("Plaintext: ", plaintext)
    print("\n=======================================================================\n")

    # Hill cipher encryption
    hill_cipher_encrypted = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"Hill Cipher output (encoded): [blue]{hill_cipher_encrypted}[/blue]")

    # Playfair cipher encryption with hard written key
    playfair_output_en = Playfair(key='ABCDEFGHIKLMNOPQRSTUVWXYZ').encipher(hill_cipher_encrypted)

    print("Playfair Cipher output (encrypted):", playfair_output_en)

    # Decrypt Playfair
    playfair_output_de = Playfair(key='ABCDEFGHIKLMNOPQRSTUVWXYZ').decipher(playfair_output_en)
    print("Playfair Cipher output (decrypted):", playfair_output_de)

    # Hill cipher decryption
    hill_cipher_decrypted = hill_cipher_decrypt(playfair_output_de, key_matrix)
    print(f"Hill Cipher output (decrypted to original plaintext): [green]{hill_cipher_decrypted}[/green]")


week_2()
