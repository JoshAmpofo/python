"""
Author: Joshua Ampofo Yentumi

Day 7 Challenge: A string Range

Description: A function that takes a single number and returns a string of its range.
             The string characters should be separated by dots.
"""


def string_range(arr):
    """
    return the range of a number as a string separated by dots

    Args:
        arr (int): single number to find range.
    
    Returns:
        arr (string): range of number separated by dots
    """
    return '.'.join(str(i) for i in range(arr))


print(string_range(6))