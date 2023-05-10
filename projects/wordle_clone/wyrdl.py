#!/usr/bin/python3
"""Stage 1 of Wyrdl"""
""" Stage 2"""

import pathlib
import random

# create a list of words to use as guess words and select them randomlu
WORDLIST = pathlib.Path("wordlist.txt")

words = [
        word.upper()
        for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
        ]

word = random.choice(words)

# ask for user input
for guess_num in range(1, 7):  # siz tries
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == word:
        print("Correct")
        break

    correct_letters = {letter for letter, correct in zip(guess, word)
                       if letter == correct}
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

else:
    print(f"The word was {word}")
