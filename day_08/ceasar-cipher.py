alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text.append(alphabet[new_index])
        else:
            encrypted_text.append(char)
    encrypted_text = ''.join(encrypted_text)
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text.append(alphabet[new_index])
        else:
            decrypted_text.append(char)
    decrypted_text = ''.join(decrypted_text)
    print(f"The decoded text is {decrypted_text}")

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("Invalid input. Please type 'encode' or 'decode'.")