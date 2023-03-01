#!/usr/bin/env python3
""" A Madlibs Game"""

# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

#madlib = f"Computer programming is so {adj}! It makes me so excited all the \
# time because I love to {verb1}. Stay hydrated and {verb2} like you are \
# {famous_person}!"

# print(madlib)

#####################################################################

""" A more interactive and random Madlibs Program"""

# import random module
import random


# Create a list of stories
stories = [ 
"Today I went to the zoo. I saw a(n) _______(adjective) _______(noun) \
jumping up and down in its tree. He _______(verb_past_tense) _______(adverb) \
through the large tunnel that led to its _______(adjective) _______(noun)!" ,
 "Yesterday I went to Disneyland. It was a(n) _______(adjective) day. I saw \
Mickey Mouse and he gave me a(n) _______(adjective) hug. Then I went on a(n) \
_______(adjective) ride that made me feel _______(emotion)!. It was so much \
fun!.",
 "Tomorrow I will go to school. I hope it will be a(n) _______(adjective) day!. \
I will learn about _______(noun_plural) and _______(noun_plural)!. Then I will \
play with my friends and we will have a(n) _______(adjective) time."
]


# pick random story from story list
story = random.choice(stories)

# split the story into words
words = story.split()

# loop through each word
for i in range(len(words)):
    # if word is a blank
    if words[i].startswith("_______"):
        # ask user for input
        prompt = words[i].replace("_______","")
        answer = input("Enter a(n) " + prompt + ": ")
        # replace the blank with input
        words[i] = answer

# join words back into a string
story = " ".join(words)

# print final story
print(story)
