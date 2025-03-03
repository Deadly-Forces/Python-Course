import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(chars)
chars = "".join(chars)

print(f"chars: {key}")
print(f"key: {chars}")

# Encryption
plain_txt = input("Enter a message to encrypt: ")
cipher_txt = ""
for letter in plain_txt:
    index = chars.index(letter)
    cipher_txt += key[index]

print(f"Original message: {plain_txt}")
print(f"Encrypted message: {cipher_txt}")

# Decryption
cipher_txt = input("Enter a message to decrypt: ")
plain_txt = ""
for letter in cipher_txt:
    index = key.index(letter)
    plain_txt += chars[index]

print(f"Original message: {cipher_txt}")
print(f"Encrypted message: {plain_txt}")