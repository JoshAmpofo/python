"""
Author: Joshua Ampofo Yentumi

Day 21 Extra Challenge: Even Number or Average

Description: A function that takes five numbers as user input and returns the largest even number in input.
             If no even number in input numbers, function returns average of all five numbers.
"""


def even_or_average() -> int:
    """
    Checks if five number inputted by user contains an even number or not

    Returns:
        int: largest even number or average of all five input numbers
    """
    count = 5
    num_list = []
    while count > 0:
        user_num = int(input("Enter a number: "))
        num_list.append(user_num)
        count -= 1
        
    # get even numbers
    even_numbers = [num for num in num_list if num % 2 == 0]
    if even_numbers:
        largest_even_number = max(even_numbers)
        return f"Largest even number in list: {largest_even_number}"
    else:
        average = sum(num_list) / len(num_list)
        return f"Average of five numbers: {average}"  # get average


print(even_or_average())