#!/usr/bin/env python3
"""
The goal of this exercise is to convert a string to a new string.
Each character in the new string is "(" if that character appearsonly once 
in original string. If that character appears more than once in the original
string, print ")". Ignore capitalization when determining if a character is a
duplicate.
"""


def duplicate_encode(word):
    """Convert string to () characters

    Arg:
        word: target string to convert

    Result:
        new string made up of ( ) characters

    Example:
        "din" => "((("
        "recede" => "()()()"
        "Success" => ")())())"
        "(( @" => "))(("
    """
    # my thinking
    # create an empty list to store new strings
    new_str = []
    # convert target string to lowercase
    low_word = word.lower()
    # loop through each character to in string
    for character in range(len(low_word)):
        # if character in string appears once, append "(" to emppty list
        if low_word[character] not in new_str:
            new_str.append("(")
            # else if character is repeated, append ")" to new list
        elif low_word[character] in new_str:
            new_str.append(")")
    # join chars together and print final result
    return "".join(new_str)


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
