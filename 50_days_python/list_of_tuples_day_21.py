"""
Author: Joshua Ampofo Yentumi

Day 21 Challenge: List of Tuples

Description: A function that takes two equal lists and combines them into a list of tuples.
             The function also checks if the input lists are of the same length.
             If not, a ValueError is raised
"""


def make_tuples(lst_1: list, lst_2: list) -> list:
    """
    Takes two equal-length lists as input and converts them into a list of tuples.
    
    Args:
        lst_1 (list): The first list of elements.
        lst_2 (list): The second list of elements.
    
    Raises:
        ValueError: If the input lists are not of equal length.
    
    Returns:
        list: A list of tuples where each tuple contains corresponding elements from lst_1 and lst_2.
    
    Example Usage:
        lst_1 = [1, 2, 3, 4]
        lst_2 = [5, 6, 7, 8]
        print(make_tuples(lst_1, lst_2))
    """
    if len(lst_1) != len(lst_2):
        raise ValueError("Lists are not of equal length")
    
    return [(x, y) for x, y in zip(lst_1, lst_2)]
        


lst_1 = [1, 2, 3, 4]
lst_2 = [5, 6, 7, 8]
print(make_tuples(lst_1, lst_2))


### ALTERNATIVE PATHWAY ###
def make_tuples(lst_1: list, lst_2: list) -> list:
    result = []
    if len(lst_1) != len(lst_2):
        raise ValueError("Input lists must be of equal length")
    for i in range(len(lst_1)):
        result.append((lst_1[i], lst_2[i]))
    return result


lst_1 = [1, 2, 3, 4]
lst_2 = [5, 6, 7, 8]
print(make_tuples(lst_1, lst_2))