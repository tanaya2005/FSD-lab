# Vigenère Cipher Encryption and Decryption

# Function to generate the repeating key (same length as plaintext)
def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# Encrypt the plaintext
def encrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        if text[i].isalpha():  # Encrypt only alphabets
            x = (ord(text[i].upper()) + ord(key[i].upper())) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)

# Decrypt the ciphertext
def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])
    return "".join(orig_text)

# Driver code
if __name__ == "__main__":
    print("Vigenère Cipher Demo\n")

    text = input("Enter the plaintext: ")
    keyword = input("Enter the key: ")

    key = generate_key(text, keyword)
    cipher_text = encrypt(text, key)
    print(f"\nEncrypted Message: {cipher_text}")

    decrypted_text = decrypt(cipher_text, key)
    print(f"Decrypted Message: {decrypted_text}")
