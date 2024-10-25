

def hash():
    plaintext =  input("enter input: ")
    hash = 0
    prime1 = 89681
    prime2 = 96079
    for char in plaintext:
        hash = (hash * prime1 + ord(char)) % (2**prime2)
        hash = str(hash)
    print(hash[32:])



hash()