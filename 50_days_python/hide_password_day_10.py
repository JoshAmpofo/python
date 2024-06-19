"""
Author: Joshua Ampofo Yentumi

Day 10 Challenge: Hide my password

Description: A function that takes no parameters and asks a user to input
             a password. The password is then hidden using * and the length
             of password returned to the user.
"""


def hide_password():
    """
    Hide a users password
    
    Returns:
        Hidden password and length of password
    """
    password = input('Enter a password: ')
    hidden_password = '*' * len(password)
    return f"Your password {hidden_password} is {len(password)} characters long"


print(hide_password())