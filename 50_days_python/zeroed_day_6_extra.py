"""
Author: Joshua Ampofo Yentumi

Day 6 Extra Challenge: Zero Both Ends

Description: Write a function that takes a list of numbers as argument 
             and zeros the first and last number in the list.
             The zeroed list is then returned
"""


def zeroed(lst):
    """
    convert elements at the beginning and ends of list to zeros

    Args:
        lst (list): numbers to convert both ends to zeros
    
    Returns:
        zeroed list
    """
    if isinstance(lst, list):
        lst[0] = 0  # convert first element to zero
        lst[-1] = 0 # convert last element to zero
        
        return lst
    else:
        return "Function requires list of numbers only"
    
    
print(zeroed([2, 5, 7, 8, 9]))
print(zeroed([1, 2, 3]))
print(zeroed([10]))
print(zeroed((1, 2, 3)))