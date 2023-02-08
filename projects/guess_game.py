#!/usr/bin/python3
"""A simple guess the number game"""

import random

count = 5
number = random.randint(1, 10)

while count > 0:
    guess = int(input("Enter a number: "))
    if guess == 5:
        print(f"That's the correct number!. You have {count} tries left")
    else:
        count -= 1
        print(f"Still trying. Number is now {guess}. {count} tries left")
    
