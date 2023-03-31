#!/usr/bin/python3
import random

"""A simple guess the number game"""


count = 5
number = random.randint(1, 11)

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
        if guess < number:
            print("Oops! That's too low. Aim higher!")
        if guess > number:
            print("uu la la! That's too high!")
        if count == 0:
            print(f"Shoot, you didn't get it right and now GAME OVER!!!.\
 The number was {number}")
        else:
            print(f"You have {count} tries left")
