"""
Author: Joshua Ampofo Yentumi

Challenge Day 26: Sort Words

Description: A function that takes a string of words as an argument, removes whitespaces,
             and returns a list of letters sorted in alphabetical order.
             Letters will be separated by commas. 
             All letters should appear once in the list (i.e. remove duplicates)
"""


def sort_words(word: str) -> list:
    """
    A function that sorts words in alphabetical order
    
    Arg(s):
        word: target string to sort
        
    Returns:
        List of sorted words in alphabetical order
    """
    # remove whitespaces and select only unique letters
    word = word.replace(" ", "")
    
    # sort in aphabetical order
    uniques = sorted(set(word)) # this returns a list
    
    # join individual letters into one main string, separated by commas
    uniques = ", ".join(uniques)
    
    # convert new string into a list
    return [uniques]
    
    
    
print(sort_words('love life'))