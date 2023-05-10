#!/usr/bin/env python3
"""In this kata, you are required to, given a string, replace every letter
   with its position in the alphabet.
   If anything in the text isn't a letter, ignore it and don't return it.
"""

# create dict to store value of each alphabet 
alph_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
                 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                 'x': 24, 'y': 25, 'z': 26
                 }

def alphabet_position(letter):
    positions = []  # list to store corresponding value of letters in dict
    for i in letter.lower():  # convert each letter to lowercase
        if i in alph_dict:  # search through dict to see if letter exists
            positions.append(str(alph_dict[i]))  # add position to list
        elif i not in alph_dict:  # if letter not in dict, skip
            continue
    return " ".join(positions)  # print positions of alphabet in target str
    

print(alphabet_position("The sunset sets at twelve o' clock."))
