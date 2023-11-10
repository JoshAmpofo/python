"""
Author: Joshua Ampofo Yentumi

Day 9 Challenge: Biggest Odd Number

Description: A function that returns the biggest odd number in a string.
             Use list comprehension
"""


def biggest_odd(number: str):
    """
    Checks a string of numbers to find the biggest number

    Args:
        number (str): string of numbers to find biggest odd number
    
    Return:
        number (int): biggest odd number in string
    """
    odd_numbers = [int(num) for num in number if int(num) % 2 != 0]
    return max(odd_numbers)


string_number = '23569'
print(biggest_odd(string_number))