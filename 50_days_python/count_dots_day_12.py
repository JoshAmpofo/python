"""
Author: Joshua Ampofo Yentumi

Day 12 Challenge: Count the Dots

Description: A function that takes a string separated by dots as a parameter
             and counts how many dots are in the string.
"""


def count_dots(strng: str) -> str:
    """
    Count the number of dots in a given string.

    Args:
        strng (str): A string containing dots.

    Returns:
        str: A string with the count of dots.
    """
    count = strng.count('.')
    return f"Number of dots in string: {count}"


print(count_dots("h.e.l.p."))