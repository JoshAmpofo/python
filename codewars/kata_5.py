#!/usr/bin/env python3
"""
In this task, you are to take a given number and arrange it in
descending order. Essentially, return the largest possible digit from the 
given input
"""


def descend(num):
    """Return number in descending order"""
    new_num = str(num)
    new_num_sorted = sorted(new_num, reverse = True)
    return int("".join(new_num_sorted))


print(descend(12345))
print(descend(54968))
print(descend(10009))
