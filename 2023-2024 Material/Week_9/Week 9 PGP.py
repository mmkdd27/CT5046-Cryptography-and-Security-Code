import gnupg
import os
from dotenv import load_dotenv

# gpg = gnupg.GPG(gpgbinary='C:\Program Files (x86)\GnuPG\bin\gpg.exe')
# If the GnuPG package isn't able to find the binary

# Load environment variables from the .env file
# This is because of the repo being publicly available
# You Could skip this section if you are writing your own

load_dotenv()
email = os.getenv('PGP_EMAIL')
passphrase = os.getenv('PGP_PASSPHRASE')
fingerprint = os.getenv('PGP_FINGERPRINT')

# Initialize GPG
gpg = gnupg.GPG()

# generate PGP Key Pair, snippet from GnuPG documentation
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


# Genrates pgp Keypair
key = generate_pgp_key()
fingerprint = key.fingerprint

# Function to sign file
def sign_file(file_path, output_signature):
    with open(file_path, 'rb') as file:
        signed_data = gpg.sign_file(file, keyid=fingerprint, passphrase=passphrase)

    # Saves the signature to an output file
    with open(output_signature, 'w', encoding='utf-8') as sig_file:
        sig_file.write(str(signed_data))
    print(f"<{file_path}> was signed. Signature saved to <{output_signature}>")


# Sign the files
sign_file('CT-Book-en.pdf', 'PDF Output.pdf.sig')
sign_file('Vigenere Cipher Matrix.png', 'Image Output.png.sig')

