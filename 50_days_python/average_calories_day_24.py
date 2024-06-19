#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Challenge Day 24: Average Calories

Description: Implement a function called `average calories` that calculates the average
             calorie intake of a user. The function should ask the user to imput their
             calorie intake for "any number of days", and once they hit "done", it should calculate and return the average intake.
"""


def average_calories() -> int:
    """Calculates the average calories of a user"""

    calories_list = []
    while True:
        try:
            calorie = input("Calories (input done to end program): ")
            if calorie == "done":
                break
            calories_list.append(int(calorie))
        except ValueError:
            return "Input Invalid. Try again"
    return f"Average calories intake: {sum(calories_list)/len(calories_list):.2f}"


if __name__ == "__main__":
    print(average_calories())
