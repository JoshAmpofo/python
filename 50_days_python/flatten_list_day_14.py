"""
Author: Joshua Ampofo Yentumi

Day 14 Challenge: Flatten The List

Description: A function that takes a nested list as argument and converts
             it into a one dimensional list
"""


def flat_list(nested_lst: list) -> list:
    """
    convert a nested list into a one dimensional list

    Args:
        nested_lst (list): nested list

    Returns:
        flat_lst (list): one dimensional list
    """
    # create an empty list
    flat_lst = []
    # iterate through nested list
    for element in nested_lst:
        # check if element is a list, recursively flatten it
        if isinstance(element, list):
            flat_lst.extend(flat_list(element))
        # if element not a list, add it to flat list
        else:
            flat_lst.append(element)
    
    return flat_lst


nested_list = [[2, 4, 5, 6]]
print(flat_list(nested_list))