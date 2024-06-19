"""
Author: Joshua Ampofo Yentumi

Day 22 Challenge: Add Under_Score

Description: Three functions that perform linked operations on a string.
             The first function takes a string and adds a hash ("#") between the words.
             The second function removes the hash ("#") and adds an underscore("_").
             The third function removes the underscore and replaces it with nothing.
"""


def add_hash(word: str) -> str:
    """
    Adds a hash in-between each character of a string.

    Args:
        word (str): The string to add hashes to.

    Returns:
        str: The string with hashes in-between.
    
    Raise:
        ValueError if input not string.
    """
    if isinstance(word, str):
        if word == '':
            return ''
        return '#'.join(word)
    else:
        raise ValueError("Input must be a string")


def add_underscore(word: str) -> str:
    """
    Replaces hashes in a string with underscores.

    Args:
        word (str): A string containing hashes.

    Returns:
        str: The input string with all hashes replaced by underscores.
    """
    return word.replace("#", "_")


def remove_underscore(word: str) -> str:
    """
    Removes any underscore in a string containing underscore.
    
    Args:
        word (str): The input string containing underscores.

    Returns:
        str: The input string with all underscore characters removed.
    """
    return word.replace("_", "")

    
word = "Python"
print(remove_underscore(add_underscore(add_hash(word))))