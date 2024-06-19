"""
Author: Joshua Ampofo Yentumi

Challenge Day 26: Sort Words

Description: A function that takes a string of words (words and spaces) as an argument. 
             Returns the length of all words in the string in the form of a dictionary.
             and returns a list of letters sorted in alphabetical order.
"""


def string_length(word: str) -> dict:
    """
    Counts the length of words in a string

    Arg(s):
        word (str): string to count

    Return:
        length of each word in string, returned as a dictionary
    """
    # create a dictionary tp store words and their lengths
    word_dict = {}

    # split target string into individual words
    words = word.split()

    # iterate through split words list and find the length of each word
    for word in words:
        word_length = len(word)
        # add word and its length to the dictionary
        word_dict[word] = word_length

    # return words and their lengths
    return word_dict


s = "Hi my name is Richard"
print(string_length(s))
