# LLM Genrated code
# TODO Implement my own version of this

def caesar_cipher(text, shift):
    result = ""

    # Convert text to lowercase
    text = text.lower()

    # Traverse the text
    for char in text:
        # Encrypt/decrypt only alphabetic characters
        if char.isalpha():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            result += char

    return result


def shift_word(word, shift):
    # Shift a single word by the given shift value
    return caesar_cipher(word, shift)


def find_and_shift_three_letter_words(ciphertext):
    words = ciphertext.split()  # Split text into words

    # First, find all three-letter words in the text
    three_letter_words = [word for word in words if len(word) == 3]

    # Now try shifting only those three-letter words
    for shift in range(26):
        shifted_words = []
        for word in words:
            if word in three_letter_words:
                shifted_word = shift_word(word, shift)
                shifted_words.append(shifted_word)
            else:
                shifted_words.append(word)

        shifted_text = ' '.join(shifted_words)

        # Check if any shifted three-letter word becomes "the"
        if "the" in shifted_words:
            print(f"Found 'the' with shift {shift}. Deciphering full text...")

            # Apply the same shift to the entire ciphertext
            deciphered_text = caesar_cipher(ciphertext, shift)
            print(f"Deciphered text: {deciphered_text}")
            return deciphered_text

    print("The word 'the' was not found in any shift.")
    return None


# Example ciphertext
ciphertext = "vtjoh b mmn efgoujmz voefsnjoft uif wbmvf pg uif sftu pg uif sfqptfupsz cvu xibu dbo pof ep cvu up dibohf xjui uif ujnft "  # Example text

# Try to find "the" by first shifting only three-letter words
find_and_shift_three_letter_words(ciphertext)
