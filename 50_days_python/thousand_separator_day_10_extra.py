"""
Author: Joshua Ampofo Yentumi

Day 10 Extra Challenge: A Thousand Separator

Description: A function that will take a list of huge numbers
             convert eacch into a string and return list with a thousand separator
"""


def convert_numbers(lst: list) -> list:
    """
    convert numbers to strings separated by a thousand separator

    Args:
        lst (list): list of positive large numbers

    Return:
        new_lst (list): list of string numbers with a thousand separator
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in lst):
        raise TypeError("Elements in the list must be numbers")
    if not lst:
        return "Input list is empty"
    new_lst = [format(num, ',') for num in lst]
    return str(new_lst)


print(convert_numbers([1000000, 2356989, 2354672, 9878098]))
print(convert_numbers([]))
print(convert_numbers(('10000', '200000')))
print(convert_numbers(['asterisk', 'comma', 'period']))