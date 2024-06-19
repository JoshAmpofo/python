"""
Author: Joshua Ampofo Yentumi

Day 12 Extra Challenge: Your Age on Minutes

Description: A function that tells a user how old they are in minutes.
             The user inouts their year of birth and their age should be returned
             in minutes by subtracting their year of birth from the current year.

             The user can only input a 4-digit year of birth. Entering any number longer
             or shorter than 4 digits should render the input invalid. User should be notified
             that they must enter a four-digit number.
             
             If a user enters a year before 1900, the code should tell the user that input is invalid.
             If user enters the year after the current year, code should tell the user to input a 
             valid year.
"""


from datetime import datetime

def age_in_minutes() -> int:
    """
    Calculates the age of a person in minutes based on their year of birth.
    
    Arg(s):
        year_of_birth (int): year of birth of user

    Returns:
        age_minutes (int): age of user in minutes
    """
    while True:
        year_of_birth = int(input('Enter your year of birth: '))
        
        # Check if the input is a four-digit number
        if year_of_birth < 1000 or year_of_birth > 9999:
            print("Invalid input. Please enter a four-digit year of birth.")
            continue

        MINIMUM_YEAR = 1900
    
        # Check if the year_of_birth is before the minimum year or after the current year
        current_year = datetime.now().year
        if year_of_birth < MINIMUM_YEAR or year_of_birth > current_year:
            print("Invalid year. Please enter a year between {} and the current year.".format(MINIMUM_YEAR))
            continue
    
        # Calculate the age in years
        age_years = current_year - year_of_birth

        # Convert the age in years to minutes (1 year = 525600 minutes)
        age_minutes = age_years * 525600

        return "You are {:,} minutes old".format(age_minutes)


print(age_in_minutes())