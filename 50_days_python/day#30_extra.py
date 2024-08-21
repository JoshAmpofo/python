#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Day 30 Extra Challenge: Sort by Last Name

Description: A function that takes a list of names and sorts the names according to 
             last names and returns the sorted names in alphabetical order, with 
             last name coming first, followed by the forst name.
             
             For example:
             ["Rey Jay", "Ama Konduah"] -> sorted_names(list) -> ['Konduah Ama', 'Jay Rey']
"""


def sorted_names(names: list) -> list:
    """
    This function takes a list of names in "First Last" format and returns a list of names sorted alphabetically by surname.

    Args:
        names (list): list of names

    Returns:
        list: sorted list of names starting with surnames, in alphabetical order
    """
    sorted_list = [", ".join(name.split()[::-1]) for name in names]
    return sorted(sorted_list)


if __name__ == "__main__":
    names = [
        "Beyonce Knowles",
        "Alicia Keys",
        "Katie Perry",
        "Chris Brown",
        "Tom Cruise",
    ]
    print(sorted_names(names))
