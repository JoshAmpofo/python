"""
Author: Joshua Ampofo Yentumi

Day 3 Extra Challenge: Lowercase Names

Description: This program takes a list of names as arguments and returns a tuple of all names
             in the list that only have lowercase letters. The names in the tuple are sorted
             alphabetically in descending order.
"""


def lowercase_names(lst: list):
    """
    checks a list of strings for lowercase names

    Args:
        lst(list): list containing string of lowercase and uppercase names
        
    Return:
        new_lst (list/tuple): new list containing lowercase names returned as a tuple
    """
    if isinstance(lst, list):
        # create an empty list
        new_lst = []
        for name in lst:  # loop through list
            if name.islower(): # check if name is lowercase
                new_lst.append(name)
        # sort the list in descending order
        new_lst.sort(reverse=True)
        return tuple(new_lst)
    else:
        return "Sorry, argument should be a list only!"
    
    
names = ['kerry', 'dickson', 'John', 'Mary', 'carol', 'Rose', 'adam']
print(lowercase_names(names))
print(lowercase_names(("Eat", "code", "sleep", "Code", "repeat")))