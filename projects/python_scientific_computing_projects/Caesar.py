"""
Project 1: Caesar Cipher
"""
text = input('Enter message to encrypt: ')
shift = int(input('Enter offset value: '))


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def caesar(message, offset):
    """
    Creates a caesar cipher

    Args:
        message (str): A string of text to be encrypted.
        offset (int): The degree of encryption, represented by the number of positions to shift the letters of the alphabet.

    Returns:
        str: The original input message.
        str: The encrypted input message.
    """
    encrypted_text = ''

    for char in message:
        if char == ' ':
            encrypted_text += char
        elif char.islower() or char.isupper():
            index = ALPHABET.find(char.lower())
            new_index = (index + offset) % len(ALPHABET)
            encrypted_text += ALPHABET[new_index].upper() if char.isupper() else ALPHABET[new_index]

    return f"Original input: {message}\nEncrypted input: {encrypted_text}"


print(caesar(text, shift))