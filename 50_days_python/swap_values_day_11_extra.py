"""
Author: Joshua Ampofo Yentumi

Day 11 Extra Challenge: Swap Values

Description: A function that takes a list of numbers and swaps the first element
             with the last element
"""


def swap_values(lst: list):
    """
    Exchanges the first element in a list with the last element.

    Args:
        lst (list): A list of numbers to swap the first and last elements.

    Returns:
        lst_copy (list): The list with the first and last elements swapped.
    """
    # create a copy of the list
    lst_copy = lst.copy()
    
    # check if list is empty or contains only 1 element
    if len(lst_copy) < 2:
        return f"Swapped elements list: {lst_copy}"
    
    # swap the first and last elements
    lst_copy[0], lst_copy[-1] = lst_copy[-1], lst_copy[0]
    
    return f"Swapped elements list: {lst_copy}"


numbers = [2, 4, 67, 7]
numbers_2 = [1]
print(f'Original list: {numbers}')
print(swap_values(numbers))
print(f'Original list: {numbers_2}')
print(swap_values(numbers_2))