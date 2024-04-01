#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Day 24 Extra Challenge: Create a Nested List

Description: Implement a function called `nested_lists` that takes any number of lists
             and creates a 2-dimensional nested list of lists.
             Check that the inputs are of the list data type. 
             If not return "Invalid arguments. Please check your arguments."
"""


def nested_lists(*args: list) -> list:
    """Creates a nested list"""
    nested = [arg for arg in args if isinstance(arg, list)]

    if len(nested) == len(args): # all items are lists
        return nested
    else:
        return "Invalid arguments. Please check your arguments: lists only"


if __name__ == "__main__":
    print(nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))
    #print(nested_lists([1, 2, 3, 4], (5, 6, 7, 8), [9, 10, 11, 12]))
