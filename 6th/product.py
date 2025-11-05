import math

# Caesar Cipher Function
def caesar_encrypt(text, shift):
    encrypted = ''
    text = text.upper()
    for ch in text:
        if ch.isalpha():  # shift only letters
            encrypted += chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted += ch
    return encrypted


# Columnar Cipher Function
def columnar_encrypt(text, key, pad='X'):
    text = text.replace(" ", "").upper()  # remove spaces
    cols = len(key)
    rows = math.ceil(len(text) / cols)

    # Pad text
    text += pad * (rows * cols - len(text))

    # Create matrix
    matrix = [list(text[i:i+cols]) for i in range(0, len(text), cols)]

    # Get order of columns based on alphabetical order of key
    key_order = sorted(list(enumerate(key.upper())), key=lambda x: (x[1], x[0]))
    col_order = [index for index, _ in key_order]

    # Read columns in order
    cipher = ''
    for col in col_order:
        for row in matrix:
            cipher += row[col]
    return cipher


# MAIN PROGRAM
plaintext = input("Enter plaintext: ")
caesar_key = int(input("Enter Caesar cipher shift (number): "))
columnar_key = input("Enter Columnar cipher key (word): ")

# Step 1: Caesar encryption
intermediate_text = caesar_encrypt(plaintext, caesar_key)
print("Intermediate text (after Caesar cipher):", intermediate_text)

# Step 2: Columnar encryption
final_cipher = columnar_encrypt(intermediate_text, columnar_key)
print("Final cipher text (after Columnar cipher):", final_cipher)
