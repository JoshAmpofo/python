from typing import List

"""
Author: Joshua Ampofo Yentumi

Challenge day 27: Unique Numbers

Desccription: A function that takes a list of numbers as an argument and finds all unique numbers in the list.
              Sum up the unique numbers and caluclate the difference between the sum of all numbers in the original list
              and the sum of all unique numbers in the unique list.
              If the difference is an "even" number, the function returns the original list.
              If the difference is "odd", the function returns a list with only unique numbers
"""


def unique_numbers(num_list: List[int]) -> List[int]:
    """
    Calculates the difference between the sum of all numbers and the sum of unique numbers in the provided list.

    Args:
    num_list (List[int]): A list of integers.

    Returns:
    List: If the difference between the sum of all numbers and the sum of unique numbers is even, returns the original list.
          If the difference is odd, returns a list containing only the unique numbers.
    """
    # Input validation to ensure num_list contains only integers
    if not all(isinstance(num, int) for num in num_list):
        raise ValueError("All elements in num_list must be integers.")

    # get unique numbers
    uniq_list = list(set(num_list))

    # get sumsand find the difference
    orig_sum = sum(num_list)

    uniq_sum = sum(uniq_list)

    # get difference
    diff = orig_sum - uniq_sum

    # return orig list if diff is even or uniq list if diff is odd
    return num_list if diff % 2 == 0 else uniq_list


list1 = [1, 2, 4, 5, 6, 7, 8, 8]  # even
list2 = [1, 2, 2, 3, 4, 5, 5]  # odd
print(unique_numbers(list1))
print(unique_numbers(list2))
