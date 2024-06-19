"""
Author: Joshua Ampofo Yentumi

Day 18 Extra Challenge: Add and Reverse

Description: A function that takes two lists as arguments, adds each corresponding number
             And reverses the outcome. 
             If lists are not of equal length, the code should return an error message "the lists are not of equal length"
"""


def add_reverse(lst_1: list, lst_2: list) -> list:
    """
    Adds the corresponding numbers in two lists and reverses the outcome

    Args:
        lst_1 (list): The first list of integers.
        lst_2 (list): The second list of integers.

    Returns:
        list: The reversed sum of the corresponding individual elements in both lists.
    """
    if len(lst_1) != len(lst_2):
        return "The lists are not of equal length"
    
    if not all(isinstance(num, int) for num in lst_1) or not all(isinstance(num, int) for num in lst_2):
        return "The lists should contain only integers"

    result = [num_1 + num_2 for num_1, num_2 in zip(lst_1, lst_2)]
    return result[::-1]


list_1 = [10, 12, 34]
list_2 = [12, 56, 78]
results = add_reverse(list_1, list_2)
print(results)