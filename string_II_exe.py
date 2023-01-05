# Capitalize the word starting with m:

# song = """When an eel grabs your arm,
# And it causes great harm,
# That's - a moray!"""

# words = song.split() # split song into list of words

# for i in range(len(words)): # iterate through split list
#     if words[i][0].startswith('m'): # check if word starts with m
#         words[i] = words[i].capitalize() # capitalize

# song = ' '.join(words) # join capitalized word with main word
# print(song)

# Print each list question with its correctly matching answer,
# in the form:
# Q: question
# A: answer

# questions = ["We don't serve strings around here. Are you a string?",
# "What is said on Father's Day in the forest?",
# "What makes the sound 'Sis! Boom! Bah!'?"
# ]
# answers = ["No, I'm a frayed knot.",
# "'Pop!' goes the weasel.",
# "An exploding sheep."]

# for string in range(len(questions)):
#     print("Q:", questions[string])
#     print("A:", answers[string])

# Write the following poem by using old-style formatting.
# Substitute the strings 'roast beef', 'ham', 'head', 
# and 'clam' into this string:
#   My kitty cat likes %s,
#   My kitty cat likes %s,
#   My kitty cat fell on his %s
#   And now thinks he's a %s

# line_1 = "My kitty cat likes %s" % 'roast beef'
# line_2 = "My kitty cat likes %s," % 'ham'
# line_3 = "My kitty cat fell on his %s" % 'head'
# line_4 = "And now thinks he's a %s" % 'clam'

# poem = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4 
# print(poem)

# Write a form letter by using new-style formatting. Save
# the following string as "letter". Assign values to variable
# strings named "salutation", "name", "product","verbed",
# "room", "animals", "percent", "spokesman", and "job title"
# Print letter with these values using letter.format()

# letter = """Dear {salutation} {name},

# Thank you for your letter. We are sorry that our {product}
# {verbed} in your {room}. Please note that it should never
# be used in a {room}, especially near any {animals}.

# Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests,
# is {percent}% less likely to have {verbed}.

# Thank you for your support.

# Sincerely,
# {spokesman}
# {job_title}"""

# salutation = "Mr."
# name = "Eight"
# product = "Liquid Nitrogen"
# verbed = "dried"
# room = "living room"
# animals = "hyenas"
# amount = "$50"
# percent = 95
# spokesman = "Albert Einstein"
# job_title = "Head Baker"

# print(letter.format(salutation="Mr", name="Eight", product="Liquid Nitrogen", verbed="dried", room="living room",
# animals="hyenas", amount = "$50", percent=95, spokesman="Albert Einstein", job_title="Head Baker"))

# State Fair Prize Winners
# first_prize = "Boaty McBoatface wins a %s" % "prize duck"
# second_prize = "Horsey McHorseface wins a %s" % "gourd"
# third_prize = "Trainy McTrainface wins a %s" % "spitz"
# print(first_prize)
# print(second_prize)
# print(third_prize)

#Using .format()
# fair_winners = """{English_submarine} from England wins a {first_prize} for best name. 
# Second placed {Australian_racehorse} from Australia wins a {second_prize} and {Swedish_train} from Sweden wins a
# {third_prize} for coming in third in the public poll to name things."""
# print(fair_winners.format(English_submarine="Boaty McBoatface", first_prize="prize duck",
# Australian_racehorse="Horsey McHorseface", second_prize="gourd", Swedish_train="Trainy McTrainface",
# third_prize="spitz")) 

# Using f-strings
first_place = "Horsey McHorseface"
second_place = "Boaty McBoatface"
third_place = "Trainy McTrainface"

first_prize = "prize duck"
second_prize = "gourd"
third_prize = "spitz"

country_1 = "Australia"
country_2 = "England"
country_3 = "Sweden"

print(f"""{first_place} from {country_1} won the {first_prize} for coming first in the public poll to name things.
First runner-up is {second_place} from {country_2} who walks away with a {second_prize}! and the second runner-up,
{third_place} from {country_3} comes away with a wonderful {third_prize}. How exciting!""")