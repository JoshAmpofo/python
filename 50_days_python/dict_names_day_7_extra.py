"""
Author: Joshua Ampofo Yentumi

Day 7 Extra: Dictionary of Names

Description: Given a list of names return all the names that starts with 'S'
             Names should be returned as a dictionary with the number of times
             the name appears.
"""


def dict_names(lst):
    """
    count names that begins with S and returns as a dictionary 

    Args:
        lst (list): list of names
    
    Returns:
        lst (dict): number of names that begin S
    """
    # create empty dictionary
    result = {}
    for name in lst:
        if name.startswith("S"):  # check if name starts with S
            if name in result:
                result[name] += 1  # append name to dict and increase count if already there
            else:
                result[name] = 1  # append name to dict and count as 1 if not there
    return result


name = ["Joseph", "Nathan", "Sasha", "Kelly",
        "Muhammad", "Jabulani", "Sera", "Patel",
        "Sera"]
print(dict_names(name))


### ALTERNATIVE METHOD ###
def dict_names(lst):
    """
    count names that begins with S and returns as a dictionary 

    Args:
        lst (list): list of names
    
    Returns:
        lst (dict): number of names that begin S
    """
    # create empty dictionary
    result = {}
    for name in lst:
        if name.startswith("S"):
            result.update({name: lst.count(name)})  # update and count name
    return result


name = ["Joseph", "Nathan", "Sasha", "Kelly",
        "Muhammad", "Jabulani", "Sera", "Patel",
        "Sera"]
print(dict_names(name))