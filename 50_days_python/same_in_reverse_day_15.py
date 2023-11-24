"""
Author: Joshua Ampofo Yentumi

Day 15 Challenge: Same in Reverse

Description: A function that takes a string and checks if reads the same in reverse.
             Returns True if same, False if not
"""


def same_in_reverse(word: str) -> bool:
    """
    Checks if a given string is the same when reversed.

    Args:
        word (str): The string to check if is the same when reversed.

    Returns:
        bool: Returns True if the input string is the same when reversed, and False otherwise.
    """
    if word is None:
        raise TypeError("Input cannot be None.")
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    
    word = word.strip()
    word = word.lower()
    
    return word == word[::-1]


print(same_in_reverse("dad"))
print(same_in_reverse("crack"))
print(same_in_reverse('Ada'))
print(same_in_reverse(None))
print(same_in_reverse(123))