"""
Author: Joshua Ampofo Yentumi

Day 9 Extra Challenge: Zeros to the End

Description: A function that takes a list as an argument and if it has zeros
             it will be moved to the end of the list and the order of the other numbers
             are maintained. If there are no zeros in the list, the function should return
             the original list, sorted in ascending order.
"""


def zeros_last(lst: list) -> list:
    """
    Moves any zero in a list ot the end of list

    Args:
        lst (list): list of numbers to check for zeros

    Returns:
        If zeros are in list, they are moved to the end and order of other numbers maintained
        If no zeros, original list is returned in ascending order

    Return Type:
        list: the modified list with zeros moved to the end
    """
    if 0 in lst:
        lst.sort(key=lambda x: x == 0) # move all zeros to the end
    else:
        lst.sort() # maintain list and sort in ascending order
    return lst


print(zeros_last([1, 4, 6, 0, 7, 0, 9]))
print(zeros_last([2, 1, 4, 7, 6]))