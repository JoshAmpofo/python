"""
Author: Joshua Ampofo Yentumi

Day 4 Extra Challenge: Index of the Longest Word

Description: Write a function that takes a list of strings and returns the index
             of the longest word in the list.
             If there is no longest word, the function should return 0
"""


def word_index(arr: list):
    """
    Checks a list and returns the index of the longest word
    in the list

    Args:
        arr (list): strings to check index of
        
    Returns:
        index of longest word
        0 if no longest word exists in list
    """
    for word in arr:
        # check if length of words are the same
        if all(len(word) == len(arr[0]) for word in arr):
            return 0
    else:
        word == len(max(arr))  # check for longest word
        return f"The longest word is at index {arr.index(word)}"  # return index of longest word
    

words1 = ['Hate', 'remorse', 'vengeance']
words2 = ["Love", "Hate"]
print(word_index(words1))
print(word_index(words2))