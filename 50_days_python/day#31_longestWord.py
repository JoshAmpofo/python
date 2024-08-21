#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Day 31: Longest Word

Description: A function that has one parameter and takes a list of words as an argument.
            The function returns the longest word from the list and the number of letters of that word.
"""


def longest_word(words: list) -> list:
    """
    Finds the longest word in a list of words and returns the word and the number of letters in it.

    Args:
        words (list): List of words to find the longest word in.

    Returns:
        list: List containing the longest word and the number of letters in it.
    """
    longest = ["", ""]  # Initialize with an empty string for the longest word

    for word in words:
        if len(word) > len(
            longest[0]
        ):  # Compare directly with the length of the longest word
            longest = [word, len(word)]  # Update both the longest word and its length

    return longest


if __name__ == "__main__":
    words = ["Java", "JavaScript", "Python"]
    result = longest_word(words)
    print(result)
