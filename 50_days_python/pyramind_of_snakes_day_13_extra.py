"""
Author: Joshua Ampofo Yentumi

Day 13 Extra Challenge: Pyramid of Snakes

Description: A function that takes a number as an argument and creates the pyramid shape using the
             number's range.
"""

from emoji import emojize

def python_snakes(num: int) -> str:
    """
    Returns a pyramid of snakes as a string

    Args:
        num (int): range of numbers to generate pyramid

    Returns:
        str: the pyramid of snakes
    """
    # loop through rows in pyramid
    for row in range(0, num):
        # loop through columns
        for column in range(num, row, -1):
            # print space
            print(end=" ")
        # add snakes
        for snake in range(0, row + 1):
            print(emojize(':snake:'), end=" ")
        print("\n")


python_snakes(7)