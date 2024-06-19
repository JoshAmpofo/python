"""
Author: Joshua Ampofo Yentumi

Day 19 Challenge: Words and Elements

Description: There are two functions. One function takes a string of words as arguments and counts how many words are in the string.
             The second function takes a string of words and counts how many elements are in the string.
"""


def count_words(sentence: str) -> str:
    """
    Counts the number of words in a given sentence.

    Args:
        sentence (str): The sentence to count the words in.

    Returns:
        str: A string that states the number of words in the sentence.
    """
    words = sentence.split()
    word_count = len(words)
    
    return f"There are {word_count} words in the sentence"
    

def count_elements(word: str) -> str:
    """
    Count the number of elements in a string, excluding whitespace.

    Args:
        word (str): The target string in which to count individual letters.

    Returns:
        str: A formatted string that states the number of characters in the string.
    """
    word = word.replace(" ", "")
    return f"The string has {len(word)} characters"
    

print(count_words("I love learning"))
print(count_elements("I love learning"))