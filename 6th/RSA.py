import random

# Step 1: Compute GCD (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Step 2: Find Modular Multiplicative Inverse
def multiplicative_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

# Step 3: Check for prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Step 4: Generate RSA key pairs
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be the same.')

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e (encryption key) such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Generate d (decryption key)
    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

# Step 5: Encrypt message
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Step 6: Decrypt message
def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Step 7: Demo
if __name__ == '__main__':
    print("RSA Cryptography Demo\n")

    # Choose two prime numbers
    p = 61
    q = 53

    print("Generating your public/private keypairs...")
    public, private = generate_keypair(p, q)
    print(f"Public key: {public}")
    print(f"Private key: {private}")

    message = input("\nEnter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    print(f"\nEncrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"\nDecrypted message: {decrypted_msg}")
