def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace J with I
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            matrix.append(ch)

    # Fill the rest of the matrix with remaining letters
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Note: no 'J'
        if ch not in used:
            matrix.append(ch)

    # Make 5x5 grid
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None


def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result


def playfair_encrypt(text, key):
    matrix = create_playfair_matrix(key)
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            cipher += matrix[row1][(col1 + 1) % 5]
            cipher += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher += matrix[(row1 + 1) % 5][col1]
            cipher += matrix[(row2 + 1) % 5][col2]
        else:
            cipher += matrix[row1][col2]
            cipher += matrix[row2][col1]

    return cipher


# MAIN PROGRAM
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted = playfair_encrypt(plaintext, key)
print("Encrypted text:", encrypted)
