"""
Author: Joshua Ampofo Yentumi

Day 4: Only floats

Description: Write a function that has two parameters and returns 2 if both are floats,
             1 if only one argument is a float, and 0 if neither argument is a float.
"""


def only_floats(a, b):
    """
    Checks if arguments provided are floats or not.

    Args:
        a (int/float): first value to check type
        b (int/float): second value to check type
    
    Returns:
        0 if argument is not float
        1 if one argument is float
        2 if both arguments are floats
    """
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


print(only_floats(12.1, 23))
print(only_floats(15.5, 12.1))
print(only_floats(1, 2))


#### ALTERNATIVE SOLUTION ###
def only_floats(a, b):
    """
    Checks if arguments provided are floats or not.

    Args:
        a (int/float): first value to check type
        b (int/float): second value to check type
    
    Returns:
        0 if argument is not float
        1 if one argument is float
        2 if both arguments are floats
    """
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0


print(only_floats(12.1, 23))
print(only_floats(15.5, 12.1))
print(only_floats(1, 2))