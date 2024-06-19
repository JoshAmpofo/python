"""
Author: Joshua Ampofo Yentumi

Day 8 Challenge: Odd and Even

Description: This function returns the difference between the largest even number
             and the smallest odd number in a list 
"""


def odd_even(lst):
    """
    returns the difference between the largest even number and smallest odd number

    Args:
        lst (list): numbers for which difference would be found
        
    Return:
        diff_num (int): difference between numbers
    """
    new_lst_even = []
    new_lst_odd = []
    for number in lst:
        if number % 2 == 0:
            new_lst_even.append(number)
        elif number % 2 != 0:
            new_lst_odd.append(number)
            
    result = max(new_lst_even) - min(new_lst_odd)
    return f"Largest even number: {max(new_lst_even)}\nSmallest odd number: {max(new_lst_odd)}\nDifference: {max(new_lst_even)} - {min(new_lst_odd)} = {result}"


print(odd_even([1, 2, 4, 6]))
print(odd_even([2, 10, 50, 3]))
print(odd_even([-2, -15, -6, -9]))