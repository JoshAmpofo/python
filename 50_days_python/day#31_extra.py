#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Day 31 Extra challenge: Create User

Description: A function that asks the user their name, age and password. These information is then saved in a dictionary.
             Once the information is saved, the function should print "User saved. Please login"
             The function should ask the user to re-enter their name and password if they don't match saved info.
             Function should keep running until the user enters the correct logging details.
"""


def create_user() -> str:
    """
    Creates login credentials for a user and saves as a dictionary.

    Return(s):
        str: Success or failure message based on correct details input.
    """
    # Get user details and store in dictionary
    name, age, password = get_user_details()
    login_details = {"name": name, "age": age, "password": password}

    # Print success message
    print("\nUser saved. Please login\n")

    # Ask user to re-enter login details
    while True:
        try:
            # Get user input
            name = input("Enter your name: ")
            password = input("Enter your password: ")

            # Validate input
            if name == login_details.get("name") and password == login_details.get(
                "password"
            ):
                print("\nLogged in successfully\n")
                break
            else:
                print("Wrong password or username. Please try again")
                continue
        except Exception as e:
            # Handle any exceptions that occur during login
            print(e)


def get_user_details() -> tuple:
    """
    Gets user details for create_user function.

    Returns:
        tuple: containing user name (str), age (int), and password (str)
    """
    # ask for user details
    try:
        # get user name
        name = input("Enter your name: ")

        # get user age and ensure it's an int
        age = int(input("Enter your age: "))

        # get user password and encrypt
        password = input("Enter a password: ")

        return name, age, password
    except ValueError:
        # if user enters invalid input for age, print error
        print("Invalid input. Age must be an int.")
    except TypeError as e:
        print(f"Type Error: {e}")


if __name__ == "__main__":
    create_user()
