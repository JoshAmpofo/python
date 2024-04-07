#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Challenge Day 25: All the Same

Description: Implement a function called `all_the_same` that takes one argument,
             a string, a list, or a tuple, and checks if all elements are the same.
             Use the `isinstance` function to check that the input data is either a
             string, a list, or a tuple, or else raise a "TypeError" that says that
             "Input must be a string, a list or a tuple".
             If the elements are the same, the function should return "True".
             If not, it should return "False"
"""


def all_the_same(arg):
    """
    Checks if the elements in args are of the same

    Arg(s):
        arg: argument to check element equality and type

    Raises:
        TypeError if arg is not string, tuple or list

    Returns:
        True: if all elements are same. False, if otherwise.
    """
    # error checks
    if not isinstance(arg, (str, list, tuple)):
        raise TypeError("Input must be a string, a list or a tuple")

    # if arg is a str
    if isinstance(arg, str):
        # check if each element is the same by using set to check for uniqueness
        return len(set(arg)) == 1

    else:
        first_element = arg[0]
        for element in arg:
            if element != first_element:
                return False
        return True


arg = 1234
arg_1 = ["Hello", "Hello", "Hello"]
arg_2 = (1, 1, 1, 1)
arg_3 = ["blue", "black", "white"]
arg_4 = (1, 2, 1)
# print(all_the_same(arg))
print(all_the_same(arg_1))
print(all_the_same(arg_2))
print(all_the_same(arg_3))
print(all_the_same(arg_4))
