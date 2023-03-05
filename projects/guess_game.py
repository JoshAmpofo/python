#!/usr/bin/python3
"""A simple guess the number game"""

import random

count = 5
number = random.randint(1, 10)

print("****** WELCOME TO GUESS-THE-NUMBER GAME ******\n")
print("The number is between 1 and 10. You only have 5 tries.\nBEGIN!!!\n")

while count > 0:
    guess = int(input("Enter a number: "))
    if guess == number:
        print(f"That's the correct number!!!. You won!,\
 and You had {count} tries left!!!")
        exit()
    else:
        count -= 1
        if count == 0:
            print(f"Shoot, you didn't get it right and now GAME OVER!!!.\
 The number was {number}")
        else:
            print(f"Wrong. You have {count} tries left")
