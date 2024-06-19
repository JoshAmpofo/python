"""
Author: Joshua Ampofo Yentumi

Day 17 Extra Challenge: Sort by Length

Description: A function that takes a list of strings as argument and sorts the strings in ascending order according to their length.
             DO NOT use built-in sort functions
"""


def sort_length(str_lst: list) -> list:
    """
    Sort list of name according to length.

    Args:
        str_lst (list): list of strings to sort.

    Returns:
        list: new list with strings sorted in ascending order
    """
    for name in range(len(str_lst)):
        for next_name in range(len(str_lst) - 1):
            # check if any of the words is longer than the other
            if len(str_lst[next_name]) > len(str_lst[next_name + 1]):
                # swap longest name for shortest name:
                str_lst[next_name], str_lst[next_name + 1] = str_lst[next_name + 1], str_lst[next_name]
    
    return str_lst


names = ['Peter', 'Jon', 'Andrew']
print(sort_length(names))                      