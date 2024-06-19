"""
Author: Joshua Ampofo Yentumi

Day 17 Challenge: User Name Generator

Description: A function that creates a username for a user.
             The function should ask a user to input their name. 
             The function the reverses the name and attaches a random number between 0 and 9 at the end of the name.
             The function then returns the username
"""

import random


def user_name() -> str:
    """
    Creates a username for a user based on their name.

    Returns:
        str: The generated username for the user.
    """
    while True:
        try:
            name = input('Enter your name (firstname preferably): ').lower()
    
            if not name.isalpha() or name == "":
                raise ValueError("Invalid name. Name cannot be empty or contain numbers")
        
            number = random.randint(0, 10)

            username = name[::-1] + str(number)

            return f'Your username is: {username}'
        except Exception as e:
            print(f'Error: {e}')
    
    
print(user_name())