"""
Author: Joshua Ampofo Yentumi

Day 5 Extra Challenge: Tuple of Student Sex

Description: Write a code that will count how many males and females are in a list of students in a school.
             Return number of males and females as a list of tuples.
"""


def count_student_gender(lst):
    """
    Counts the number of student gender in a school list

    Args:
        lst (list): list of student gender
    
    Returns:
        number of male and female in list of tuples
    """
    count_male = 0
    count_female = 0
    for word in lst:
        if word.lower() == 'male':
            count_male += 1 
        elif word.lower() == 'female':
            count_female += 1
    
    result = [("Male", count_male), ("female", count_female)]
    return f"Gender of students in school are: {result}"


students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male',
            'female']
print(count_student_gender(students))