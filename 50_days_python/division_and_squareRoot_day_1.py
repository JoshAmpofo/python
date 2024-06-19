"""
Author: Joshua Ampofo Yentumi
Purpose: Improving my python skills by solving a python challenge a day
using the 50 Days of Python book by Benjamin Bennett Alexander

Day One: Division and Square-root

Project Description: This program takes a number as an argument and returns the 
squareroot of the number is divisible by 5 or the remainder if not
"""
def divide_or_square(num):
    """
    Returns the squareroot or remainder if arg is divisble by 5 or not
    Args:
        num (int): number to check divisibility by 5
    
    Returns:
        squareroot of number or remainder of number
    """
    from math import sqrt
    if num % 5 == 0:
        return f"Square root of {num} is {sqrt(num):.2f}"
    else:
        return f"Remainder of {num} / 5 is {num % 5}"

# call function
print(divide_or_square(100))