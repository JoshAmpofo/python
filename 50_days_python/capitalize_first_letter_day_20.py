"""
Author: Joshua Ampofo Yentumi

Day 20 Challenge: Capitalize First Letter

Description: This function takes a string as an argument and capitalizes the first letter of each word.
"""


def capitalize(word: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        word (str): The string to be capitalized.

    Returns:
        str: The input string with the first letter of each word capitalized.
    """
    # error handling
    if word is None:
        return ""
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    
    # remove leading and trailing whitespaces
    word = word.strip()
    
    # caapitalize first letter of each word
    return ' '.join(word[0].upper() + word[1:].lower() for word in word.split())


print(capitalize("i love learning"))
#print(capitalize(""))
#print(capitalize(234))