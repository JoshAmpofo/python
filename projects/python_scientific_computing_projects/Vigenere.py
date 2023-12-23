"""
Project 1b: Vigenere Cipher
"""

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def vigenere(message, key, direction=1):
    """
    Create a vigenere cipher

    Args:
        message (str): target message to encrypt
        key (str): encryption key

    Returns:
        str: encrypted message
    """
    key_index = 0
    final_message = ''
    
    for char in message.lower():
        # Append any non-letter characcter to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            
            # Define the offset and encrypted/decrypted letter
            offset = ALPHABET.index(key_char)
            index = ALPHABET.find(char)
            new_index = (index + offset * direction) % len(ALPHABET)
            final_message += ALPHABET[new_index]
    
    return final_message

def encrypt(message, key):
   return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)


print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')