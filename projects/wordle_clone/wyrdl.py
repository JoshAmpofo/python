#!/usr/bin/python3
"""Stage 1 of Wyrdl"""

# ask for user input
guess = input("Guess a word: ").upper()
if guess == "SNAKE":
    print("Correct")
else:
    print("Wrong")
