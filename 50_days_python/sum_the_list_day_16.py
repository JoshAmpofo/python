"""
Author: Joshua Ampofo Yentumi

Day 16 Challenge: What's My Age?

Description: A function that takes a nested list of integers as an argument and returns the sum of the integers.
"""


def sum_list(nest_lst: list) -> int:
    """
    Sums the integers in a nested list

    Args:
        nest_lst (list): A nested list of integers to sum.

    Returns:
        int: The sum of all the integers in the nested list.
    """
    # initialize sum variable
    nest_sum = 0
    
    # check if nest_lst is a list
    if isinstance(nest_lst, list):
        # loop through items in outer list of nested list
        for lst in nest_lst:
            # check if item in outer list of nested_list is a list
            if isinstance(lst, list):
                # loop through inner items of outer list
                for element in lst:
                    # check if element is an integer
                    if isinstance(element, int):
                        # sum items of inner list
                        nest_sum += element
    # if not nested list                    
    else:
        return 0
    
    return nest_sum


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))