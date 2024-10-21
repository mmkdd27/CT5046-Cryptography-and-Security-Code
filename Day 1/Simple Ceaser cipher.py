# first in class challenge for day 1

def chall_1():
    plaintext = input("please enter your plaintext: ")
    shift_int = int(input("Enter the cipher key (How many letters should the text be shifted ?): "))

    ciphertext = ""
    # preformatting the text
    # given more time I would have implemented a different formatting method
    # to preserve capitalization
    plaintext = plaintext.lower()

    for i in plaintext:
        if i.isalpha():# check for latin characters using pythons built-in function
            ciphertext += chr((ord(i) + shift_int-97) % 26+97) # Append the string with the shifted letter, used to mod operator to keep the numbers in the range of 97 to 122(ASCII  lower case letters)
        else:
            ciphertext += i

    print(ciphertext)


chall_1()
