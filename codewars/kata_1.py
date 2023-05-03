#!/usr/bin/env python3

# Write a function that reverses words that have letters greater than 5

def spinWords(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)

print(spinWords( "Hey fellow warriors" ))
print(spinWords( "This is a test" ))
print(spinWords ("This is another test" ))
