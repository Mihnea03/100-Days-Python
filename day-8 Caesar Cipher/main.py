# Caesar Cipher
# Munteanu Mihnea @ Mihnea03

import string

def encode(message, shift_number):
    encrypted_message = ""

    for letter in message:
        position = string.ascii_lowercase.index(letter)
        new_position = (position + shift_number) % 26
        encrypted_message += string.ascii_lowercase[new_position]
    
    return encrypted_message

def decode(message, shift_number):
    decrypted_message = ""

    for letter in message:
        position = string.ascii_lowercase.index(letter)
        new_position = (position - shift_number) % 26
        decrypted_message += string.ascii_lowercase[new_position]
    
    return decrypted_message

def main():
    print("Caesar Cipher\n")

    type_of_crypt = str(input("Do you want to encode or decode a message? Type \"encode\" or \"decode\"\n")).lower()
    message = str(input("Type your message:\n")).lower()
    shift_number = int(input("Enter the shift number:\n"))

    if type_of_crypt == 'encode':
        encoded = encode(message, shift_number)
        print(f"Your encoded message is: {encoded}")
    elif type_of_crypt == 'decode':
        decoded = decode(message, shift_number)
        print(f"Your decoded message is: {decoded}")

if __name__ == '__main__':
    main()