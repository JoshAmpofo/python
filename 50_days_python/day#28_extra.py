"""
Author: Joshua Ampofo Yentumi

Challenge 28 Extra: Largest Number

Description: A function that takes a list of integers and rearranges the individual digits to create the largest number possible.
             The number should be returned as an integer.
"""
import sys
from typing import List


def largest_number(num: List[int]) -> int:
    """
    Rearrange the individual digits of a list of integers to create the largest number possible.

    Args:
        num (List[int]): List of integers

    Returns:
        int: Largest number formed by rearranging the integers.
    """
    # Create a new list to append new number arrangement
    new_list = []
    
    # Convert each integer to a string and append to new list
    try:
        for num_str in map(str, num):
            new_list.append(num_str)
    
        # Sort the numbers based on their ASCII position in descending order
        new_list.sort(reverse=True)
    
        # Join the sorted numbers to form the largest number
        return int(''.join(new_list))
    except ValueError:
        print("Function takes only numeric inputs!. Provide correct input type")
        sys.exit()


if __name__ == "__main__":
    result = largest_number([3, 30, 34, 5, 9])
    #result = largest_number([4, "a", 5, "b"])
    print(f'{result:,}')