#!/usr/bin/python3.10

"""
author: joshua ampofo yentumi

file description: extra challenge in day 1 of 50 days of python


program description: write a function **longest_value** that takes
a dictionary as argument and returns the first longest value in dictionary
"""


def longest_value(dict):
    """
    args:
        dict (strings): holds keys for which to determine longest
                        value
    return:
        first longest value
    """
    if not dict:
        return None

    long_value = max(dict.values(), key=len)
    return long_value


print(longest_value({'fruit':'apple', 'color':'green'}))
