"""
Author: Joshua Ampofo Yentumi

Day 6 Challenge: Username Generator

Description: Write a function that generates a username from the user's email.
             The code should return everything before the @ sign as the username.
"""


def username():
    """
    generates a username from user input email

    Args:
        email (string): user email
    
    Returns:
        username before @ sign
    """
    email_input = input("Enter your email: ")
    username = email_input.split('@')[0]
    return f"Your username is: {username}"


print(username())


### ALTERNATIVE SOLUTION (USE REGEX) ###
import re
def username_regex():
    """
    generates a username from user input email

    Args:
        email (string): user email
    
    Returns:
        username before @ sign
    """
    email_input = input("Enter your email: ")
    username = re.split('@', email_input)[0]
    return f"Your username is: {username}"


print(username_regex())