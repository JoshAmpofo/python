"""
Author: Joshua Ampofo Yentumi

Day 12 Challenge: Count the Dots

Description: A function that takes a string separated by dots as a parameter
             and counts how many dots are in the string.
"""


def count_dots(strng: str) -> int:
    """
    Count the number of dots in a given string.

    Args:
        strng (str): A string containing dots.

    Returns:
        count (int): the count of dots in string.
    """
    # Outlier handling
    if strng is None or not isinstance(strng, str):
        return "Invalid input. Please provide a valid string."
    if strng == '':
        return 'Number of dots in string: 0'
    
    count = 0 #initialize counter
    for char in strng:
        if char == '.':  # iterate through string and check for dot
            count += 1  # increment counter if dot encountered
            
    return f"Number of dots in string: {count}"


print(count_dots("h.e.l.p."))