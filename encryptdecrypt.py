def encrypt(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                shifted = chr((ord(c) - ord('A') + key) % 26 + ord('A'))
            elif c.islower():
                shifted = chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            ciphertext += shifted
        else:
            ciphertext += c
    return ciphertext

def decrypt(ciphertext, key):
    decryptedtext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                shifted = chr((ord(c) - ord('A') - key + 26) % 26 + ord('A'))
            elif c.islower():
                shifted = chr((ord(c) - ord('a') - key + 26) % 26 + ord('a'))
            decryptedtext += shifted
        else:
            decryptedtext += c
    return decryptedtext


def main():
    message = input("Enter message to encrypt: ")
    key = int(input("Enter shift value (1-25): "))

    # Validate key
    if key < 1 or key > 25:
        print("Invalid shift value. Please enter a value between 1 and 25.")
        return

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
