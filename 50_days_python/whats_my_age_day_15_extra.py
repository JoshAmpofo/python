"""
Author: Joshua Ampofo Yentumi

Day 15 Extra Challenge: Whaat's My Age?

Description: A function that asks a student to enter their name, and returns their age.
             If the name is not in the dictionary database, the function will ask for their age.
             The name and age will be added to the database and then returned to the user.
"""


def your_age() -> str:
    """
    Checks a database for user's age and returns their age with a greeting

    Returns:
        str: A greeting with the user's name and age.
        
    Example Usage:
        Enter your name: jane
        Hi, Jane, you are 23 years old.

        Enter your name: kerry
        Hi, Kerry, you are 45 years old.

        Enter your name: john
        Enter your age: 30
        Hi, John, you are 30 years old.
    """
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    
    name = input("Enter your name: ").lower()
    
    if name in names_age.keys():
        return f"Hi, {name.title()}! You are {names_age[name]} years old." # alternative: {names_age.get(key)}
    elif name not in names_age.keys():
        age = int(input("Enter your age: "))
        # update dictionary
        names_age[name] = age # alternative: names_age.update(name: age)
        return f'Hi, {name.title()}! You are {names_age[name]} years old.' # alternative: {names_age.get(key)}
        

print(your_age())