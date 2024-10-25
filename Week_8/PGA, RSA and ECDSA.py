import gnupg
import os
from dotenv import load_dotenv
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import pkcs1_15, DSS
from Crypto.Hash import SHA256

# Initialize GPG (Path set only if binary location is required)
gpg = gnupg.GPG()

# Load environment variables from the .env file
# This is because of the repo being publicly available
# You could skip this section if you are writing your own

load_dotenv()
email = os.getenv('PGP_EMAIL')
passphrase = os.getenv('PGP_PASSPHRASE')
fingerprint = os.getenv('PGP_FINGERPRINT')


# Generate PGP Key Pair, snippet from GnuPG documentation
def generate_pgp_key():
    input_data = gpg.gen_key_input(
        name_email=email,
        passphrase=passphrase,
        key_type='RSA',
        key_length=2048
    )
    key = gpg.gen_key(input_data)
    print(f"PGP Key Pair fingerprint: {key.fingerprint}")
    return key


# Generate PGP Key Pair
key = generate_pgp_key()
fingerprint = key.fingerprint


# signs file with GPG
def sign_file(file_path, output_signature):
    with open(file_path, 'rb') as file:
        signed_data = gpg.sign_file(file, keyid=fingerprint, passphrase=passphrase)

    with open(output_signature, 'w', encoding='utf-8') as sig_file:
        sig_file.write(str(signed_data))
    print(f"<{file_path}> was signed. Signature saved to <{output_signature}>")


# generates ECDSA signature
def sign_file_ecdsa(file_path, output_signature):
    private_key = ECC.generate(curve='P-256')
    signer = DSS.new(private_key, 'fips-186-3')

    with open(file_path, 'rb') as file:
        data = file.read()
        hash_obj = SHA256.new(data)
        signature = signer.sign(hash_obj)

    with open(output_signature, 'wb') as sig_file:
        sig_file.write(signature)
    print(f"<{file_path}> was signed with ECDSA. Signature saved to <{output_signature}>")


# RSA
def sign_file_rsa(file_path, output_signature):
    private_key = RSA.generate(2048)
    signer = pkcs1_15.new(private_key)

    with open(file_path, 'rb') as file:
        data = file.read()
        hash_obj = SHA256.new(data)
        signature = signer.sign(hash_obj)

    with open(output_signature, 'wb') as sig_file:
        sig_file.write(signature)
    print(f"<{file_path}> was signed with RSA. Signature saved to <{output_signature}>")


# Sign files with PGP, ECDSA, and RSA
sign_file('CT-Book-en.pdf', 'PDF Output.pdf.sig')
sign_file_ecdsa('CT-Book-en.pdf', 'PDF Output ECDSA.sig')
sign_file_rsa('CT-Book-en.pdf', 'PDF Output RSA.sig')

sign_file('Vigenere Cipher Matrix.png', 'Image Output.png.sig')
sign_file_ecdsa('Vigenere Cipher Matrix.png', 'Image Output ECDSA.sig')
sign_file_rsa('Vigenere Cipher Matrix.png', 'Image Output RSA.sig')
