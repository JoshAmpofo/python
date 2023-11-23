"""
Author: Joshua Ampofo Yentumi

Day 14 Extra Challenge: Teacher's Salary

Description: A program that will calculate teachers' salaries.
            The program ask the user to enter the teacher's name, number of periods
            taught in a month and the rate per period. Overtime is $25 per period.
            The program should return the teacher's name, periods taught and gross salary
"""

# constants
MONTHLY_RATE_PER_PERIOD = 20
STANDARD_HOURS_PER_MONTH = 100
OVERTIME_RATE = 25

# auxiliary function
def calculate_gross_salary(periods):
    """
    Calculates the gross salary based on the number of periods taught, including overtime.

    Args:
        periods (int): The number of periods taught.

    Returns:
        int: The gross salary.
    """
    if periods > STANDARD_HOURS_PER_MONTH:
        overtime_period = periods - STANDARD_HOURS_PER_MONTH
        overtime_salary = (OVERTIME_RATE * overtime_period)
        gross_salary = STANDARD_HOURS_PER_MONTH * MONTHLY_RATE_PER_PERIOD + overtime_salary
    else:
        gross_salary = MONTHLY_RATE_PER_PERIOD * periods

    return gross_salary

# main function
def your_salary():
    """
    Calculates a teacher's salary based on the number of periods taught, including overtime.

    Returns:
        formatted string containing the teacher's name, number of periods taught, and gross salary.
    """
    teach_name = input("Enter Teacher's name: ").title()
    periods = int(input("Enter number of periods taught: "))

    gross_salary = calculate_gross_salary(periods)

    return f"\nTeacher: {teach_name}\nPeriods: {periods}\nGross Salary: ${gross_salary:,}"


print(your_salary())