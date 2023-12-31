"""
Project 5: Build a Password Generator using Regular Expressions
"""

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1) -> str:
    """
    Generate a random password
    
    Args:
        length (int): length of password
        nums (int): number char constraints to include in password
        uppercase (str): uppercase char constraints to include in password
        lowercase (str): lowercase char constraints to include in password
        special_chars (str): special char constraints to include in password
    
    Returns:
        password (alphanum): generated password 
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