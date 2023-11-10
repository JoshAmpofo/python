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
    if not number:
        return "Input string is empty"
    
    if not number.isdigit():
        raise ValueError("Input must only contain digits")
    
    odd_numbers = [num for num in number if int(num) % 2 != 0]
    if not odd_numbers:
        return "No odd numbers found"
    
    return f"Biggest odd number is: {max(odd_numbers)}"


string_number = '23569'
print(biggest_odd(string_number))
print(biggest_odd(""))
print(biggest_odd('abcdef'))