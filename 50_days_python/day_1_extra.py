#!/usr/bin/python3.10

"""
Author: Joshua Ampofo Yentumi

Day One Extra Challenge: Longest Value

Project Description: This program takes a dictionary as an argument and returns the first 
longest value in dictionary
"""


def longest_value(dict):
    """
    Args:
        dictionary (dict): dictionary to check for longest value
    Returns:
        longest_value (str): longest value in dictionary
    """
    if not dict:
        return None

    long_value = max(dict.values(), key=len)
    return long_value


print(longest_value({'fruit':'apple', 'color':'green'}))
