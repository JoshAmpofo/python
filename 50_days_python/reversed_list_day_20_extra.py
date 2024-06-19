"""
Author: Joshua Ampofo Yentumi

Day 20 Extra Challenge: Reversed List

Description: Given a string of words, some of which contain uppercase letters.
             Return a list of all the words that have an uppercase letter.
             Each word in the list should be reversed.
"""

import re


def reverse_char(word: str) -> list:
    """
    Searches a string for words containing capital letters 
    and returns a list of these words in reverse.

    Args:
        word (str): string containing words with some capitalized letters.

    Returns:
        list: list of words that contain capitalized letters in reverse.
    """
    # extract all words from input string
    words = re.findall(r"\w+", word)
    # filter extracted words to check for those containing uppercase letters
    result = [word[::-1] for word in words if re.search(r"[A-Z]", word)]
    
    return result
    

str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
print(reverse_char(str1))