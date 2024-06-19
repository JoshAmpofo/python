#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Challenge day 23 Extra: Multiply words

Description: Write a function that takes a string as an argument and multiplies the length of each word in the string
             by the length of each word in the string.
             Your function should only multiply words with all lowercase letters.
             If a word has one uppercase letter, it should be ignored.
"""
def multiply_words(s: int) -> int:
    """
    multiply length of lowercase words
    
    Arg(s):
        s (str): strings to multiply
    
    Results:
        int: dot product of length of individual words in strings 
    """
    length = 1
    for word in s.split():
        if word.islower():
            length *= len(word)
    return f"Product of words: {length}"


if __name__ == "__main__":
    string_1 = "love live and laugh"
    string_2 = "Hate war love Peace"
    print(multiply_words(string_1))
    print(multiply_words(string_2))