#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Challenge Day 30: Repeated Name

Description: A functon that finds the most repeated name in a list.
             The function returns a tuple of the name and how many times it appears
"""


def repeated_name(names: list) -> tuple:
    """
    Counts the number of repeated names in a list and returns the most repeated number

    Arg(s):
        names (list): list of names

    Returns:
        tuple: name and number of times it appears
    """
    # create a dictionary to store the count of each name
    name_count = {}
    # iterate over list and update the count of each name
    for name in names:
        name_count[name] = name_count.get(name, 0) + 1
    # find the name with the highest count
    most_repeated = max(name_count, key=name_count.get)
    # return results
    return (most_repeated, name_count[most_repeated])


if __name__ == "__main__":
    names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    result = repeated_name(names)
    print(result)
