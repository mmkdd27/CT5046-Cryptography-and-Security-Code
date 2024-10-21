from rich import print

from pycipher import ADFGVX, Autokey

def week_3():
    print("Task:")
    print("Create a CryptTool project which accepts a plaintext, and")
    print("◙ First encrypts it using [green]ADFGVX Cipher[/green")
    print("◙ Then encrypts the [green]ADFGVX Cipher[/green] with [green]Vernam Cipher[/green]")
    print("◙ Then gets the original plaintext back to its original form")
    print("Please input the plaintext:")

    # take input text and keywords
    plaintext = input()
    print("Please input [green]ADFGVX cipher[/green] key:")
    adfgvx_key = input()

    Polybius_square = "phqgmeaynofdxkrcvszwbutil0123456i789"  # Polybius square for ADFGVX cipher

    print("Please input [green]Vernam cipher[/green] key: ")
    vernam_key = input()

    print("\n=======================================================================\n")

    # encrypt text with ADFVX cipher
    print("encrypting text with ADFVX cipher:")
    print(f"plaintext: [blue]{plaintext}[/blue]")
    print(f"keyword: [red]{adfgvx_key}[/red]")
    print(f"predefined Polybius square : [red]{Polybius_square}[/red]")

    adfgvx_encrypted = ADFGVX(Polybius_square, adfgvx_key).encipher(plaintext)
    print(f"ADFGVX Cipher Text: [purple]{adfgvx_encrypted}[/purple]")
    print("\n=======================================================================\n")

    # encrypt text with vernam cipher
    print("encrypting text with [green]vernam cipher[/green]:")
    print(f"plaintext ([green]ADFGVX Cipher[/green] Text): [purple]{adfgvx_encrypted}[/purple]")
    print(f"keyword: [red]{vernam_key}[/red]")
    vernam_cipher = Autokey(vernam_key)
    vernam_encrypted = vernam_cipher.encipher(adfgvx_encrypted)
    print(f"Vernam Encrypted Text: [red]{vernam_encrypted}[/red]")
    print("\n=======================================================================\n")

    print("Starting decryption process")
    # decrypt ciphertext with vernam cipher
    print(f"cipher text: [purple]{vernam_encrypted}[/purple]")
    print(f"keyword: [red]{vernam_key}[/red]")

    vernam_decrypted = vernam_cipher.decipher(vernam_encrypted)
    print(f"After Vernam Decryption (ADFGVX Cipher Text): [purple]{vernam_decrypted}[/purple]")
    print("\n=======================================================================\n")
    # decrypt cipher text with ADFVX cipher
    print(f"cipher text: [purple]{vernam_decrypted}[/purple]")
    print(f"keyword: [red]{adfgvx_key}[/red]")
    print(f"predefined Polybius square : [red]{Polybius_square}[/red] ")

    adfgvx_decrypted = ADFGVX(Polybius_square, adfgvx_key).decipher(vernam_decrypted)
    print(f"Original Plaintext: [blue]{adfgvx_decrypted}[/blue]")

week_3()