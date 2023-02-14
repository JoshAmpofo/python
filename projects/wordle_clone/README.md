# Command line clone of Wordle Game using Python and RICH

Thw Wordle game is a word-guessing game created by Josh Wardle in Oct 2021.
This clone version uses the command line and the Rich library to make the game interactive for users.
The tutorial used for the game is from Real Python [link here](https://realpython.com/python-wordle-clone/).
This variant is called **Wyrdl**

## General Rules of the Game
- six attempts to guess a secret five-letter word
- after each guess you get feedback about which letters are correctly placed, which are misplaced or which are wrong
	- green means letters are correct and rightly placed
	- (https://placehold.it/150/ffffff/ff0000?text=yellow) means letters are correct but misplaced
	- gray means letters are wrong

## Aim of the Project

The goal of this project is to help me develop proficiency and comfort using concepts like: 
- `input` to read user input from the terminal 
- `if statements` to check different conditions 
- `for` and `while` loops to repeat actions
- Organize data in `structures` like `lists` and `dicitionaries`
- Encapsulate code with `functions`

## Actionable steps

- Create a simple **prototype** that allows a user to guess a secret word and gives feedback on individual letters
- Add a **list of words** that the game randomly chooses from in order to make it interactive
- Refactor the code to use **functions**.
- Add **color** and **style** to the game using the Rich library
- Provide **actionable** **feedback** to users when they play the game
- Improve the user interface by adding the **status of all the letters** in the alphabet
