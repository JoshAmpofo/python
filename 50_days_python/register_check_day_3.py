"""
Author: Joshua Ampofo Yentumi

Day Three: Register Check

Description: This program checks the number of students
             present in school by counting the number of 
             students with yes. 
             The function will return the number of students
"""


def register_check(arr: dict):
    """
    checks the number of students present in school

    Args:
        arr (dict): dictionary of student attendance

    Return:
        count (int): number of students present in school
    """
    if isinstance(arr, dict):
        # initialize counter
        count = 0 
        # loop through dictionary and check if value is yes
        for value in arr.values():
            if value == "yes":
                count += 1  # count number of yeses
        return count 
    else:
        return "Only a dictionary argument is required!"


register = {'Michael': 'yes', 'John': 'no', 
            'Peter': 'yes', 'Mary': 'yes'}


print(register_check(register))
print(register_check(('yes','no','yes','yes')))
print(register_check(['yes', 'no', 'yes', 'no']))