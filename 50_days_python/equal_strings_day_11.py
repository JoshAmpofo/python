"""
Author: Joshua Ampofo Yentumi

Day 11 Challenge: Are They Equal

Description: A function that takes two strings as arguments and compares them.
             If both strings are equal (have the same characters and equal length), it should return True
             If not, it should return False
"""


def equal_strings(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams by comparing their lengths and unique characters.

    Args:
        s1 (str): The first string to check for anagrams.
        s2 (str): The second string to check for anagrams.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) == len(s2)


print(equal_strings("love", "evol"))
print(equal_strings("lanch", "lunch"))
print(equal_strings('BOXES', 'boxes'))