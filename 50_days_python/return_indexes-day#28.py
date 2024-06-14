"""
Author: Joshua Ampofo Yentumi

Challenge day 28: Return Indexes

Description: A function that takes a string as a parameter and returns the positions
             or indexes, of all lowercase letters in the string.
"""


def index_position(text: str) -> list:
    """
    Returns the indexes of lowercase letters in a string.
    
    Arg(s):
        text (str): string to return indexes of lowercase letters
        
    Returns:
        list of indexes
    """
    return [text.index(letter) for letter in text if letter.islower()]


print(index_position("LovE"))