"""
Author: Joshua Ampofo Yentumi

Day Two: Strings to Integers

Project Description: This program takes a list of strings as argument 
                     converts them to Integers and sums the list.
"""


def convert_add(lst=[]):
    """
    Args:
        lst(strings): contains strings to convert to integers
        
    Return:
        num_list(int): sum of integer converted items
    """
    if isinstance(lst, list):
        num_list = []
        
        for string in lst:
            new_list = int(string)  # convert each element to integer
            num_list.append(new_list)  # add converted items to new list
        return sum(num_list)  # sum each element and return results
    else:
        return "Error: Input must be a list"

    
print(convert_add(["1", "3", "5"]))
# check other data structures
print(convert_add(("1","2","3"))) # tuple
print(convert_add({"1","2","3"})) # dictionary