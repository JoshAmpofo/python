"""
Author: Joshua Ampofo Yentumi

Day 18 Challenge: Any Number of Arguments

Description: A function that can receive any number of positional arguments (integers and floats).
             Return the average of the integers (positional arguments)
"""


def any_number(*args):
    """
    Takes any number of arguments (integers or floats)
    
    Returns:
        average of the arguments
    """
    sum_args = sum(args)
    count_args = len(args)
        
    average = sum_args / count_args if count_args != 0 else 0
        
    return average


#print(any_number(12, 90, 12, 34))
print(any_number(12, 90))