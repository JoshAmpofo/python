"""
Project 5: Build a Password Generator using Regular Expressions
"""

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1) -> str:
    """
    Generate a random password based on the given constraints.

    Args:
        length (int): The length of the password.
        nums (int): The number of numbers to include in the password.
        special_chars (int): The number of special characters to include in the password.
        uppercase (int): The number of uppercase letters to include in the password.
        lowercase (int): The number of lowercase letters to include in the password.

    Returns:
        password (str): The generated password that satisfies all the given constraints.
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # concatenate all characters
    all_characters = letters + digits + symbols
    
    while True:
        password = ''
        # Generate password
        for _ in range(length):
            # add random character to password
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]')
        ]
        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints
        ):
            break
    
    return password


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)