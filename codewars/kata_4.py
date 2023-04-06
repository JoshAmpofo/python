#!/usr/bin/env python3
"""
In this kata, you'll create a function that takes a list of non-negative
integers and strings and returns a new list with the strings filtered out.
"""


def filter_list(l):
    """Return a new list with the strings filtered out"""
    # create new list
    new_l = []
    # iterate through each item in l arg and check if item is str or not
    for item in l:
        if type(item) == int:
            new_l.append(item)
        else:  # if not, skip item
            continue
    return new_l   # return new_l without strings


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))

# using list comprehension
def filter_list(l):
    """comment here"""
    return [item for item in l if type(item) == int ]

print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
