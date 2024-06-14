"""
Author: Joshua Ampofo Yentumi

Challenge 27 Extra: Difference of Two Lists

Description: A function that takes two lists as arguments.
             Function should return all elements that are in list a but not in list b
             and all elements in list b but not in list a.
             Use List comprehensions
"""


def difference_of_two_lists(a, b):
    """
    Takes two lists and returns another list containing elements not present in both lists
    
    Arg(s):
        a (list): first list
        b (list): second list
        
    Returns:
        list containing elements not present in a or b
    """
    # get unique elements in a
    a_uniqs = [item for item in a if item not in b]
    # get unique elements in b
    b_uniqs = [item for item in b if item not in a]
    # return concat of both lists
    return a_uniqs + b_uniqs
    
# Example usage
a = [1, 2, 4, 5, 6]
b = [1, 2, 5, 7, 9]
result = difference_of_two_lists(a, b)
print(result)