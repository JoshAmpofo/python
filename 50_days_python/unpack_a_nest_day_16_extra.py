"""
Author: Joshua Ampofo Yentumi

Day 16 Extra Challenge: Unpack a Nest

Description: This program generates a list of numbers in a nested list without duplicates
"""


def unpack(nested_list: list) -> list:
    """
    Unpacks a nested list of numbers without duplicates.

    Args:
        nested_list (list): nested list to unpack

    Returns:
        list: flat list without duplicates
    """
    output_list = list(set([num for sublist in nested_list for num in sublist if num in [34, 67, 78]]))
    return output_list


nested_list = [[12, 34, 56, 67], [34, 68, 78]]
print(unpack(nested_list))