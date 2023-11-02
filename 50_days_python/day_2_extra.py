"""
Author: Joshua Ampofo Yentumi

Day 2 Extra: Duplicate Names

Description: This program takes a list of strings as arguments
             and checks if there are duplicate strings in the list.
             If there are duplicates in list, the duplicates are returned
             else no duplicates are returned.
"""


def check_duplicates(lst=[]):
    """
    checks a list of strings for duplicates

    Args:
        lst(list): list containing strings
        
    Return:
        new_lst (list): new list containing duplicates if any, else an empty list
    """
    if isinstance(lst, list):
        new_lst = []
        seen_str = set()  # store duplicate strings
        for word in lst:
            if word in seen_str:  # if word appears more than once
                new_lst.append(word)
            else:
                seen_str.add(word)  # store word only once
        return new_lst  # duplicate or empty
    else:
        return "Sorry, argument should be list only!" 
    

fruits = ["apple", "orange", "banana", "apple", "banana"]
names = ["Yoda", "Moses", "Joshua", "Mark"]

print(check_duplicates(fruits))
print(check_duplicates(names))
print(check_duplicates(("Eat", "Code", "Sleep", "Code", "Repeat")))