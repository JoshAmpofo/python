"""
Author: Joshua Ampofo Yentumi

Day 21 Extra Challenge: Even Number or Average

Description: A function that takes five numbers as user input and returns the largest even number in input.
             If no even number in input numbers, function returns average of all five numbers.
"""


def even_or_average() -> int:
    """
    Checks if five numbers inputted by user contains an even number or not.

    Returns:
        int: largest even number or average of all five input numbers.
    """
    # get 5 numbers from user and add to list
    num_list = []
    for _ in range(5):
        user_num = int(input("Enter a number: "))
        num_list.append(user_num)
    # filter for even numbers    
    even_numbers = list(filter(lambda num: num % 2 == 0, num_list))
    # find largest even number
    if even_numbers:
        largest_even_number = max(even_numbers)
        return f"Largest even number in input: {largest_even_number}"
    # find average
    else:
        average = sum(num_list) / len(num_list)
        return f"Average of five numbers: {average}"


print(even_or_average())