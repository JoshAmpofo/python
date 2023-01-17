# Create dictionary
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# Create quotes
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses"
}
print(bierce)

# Create with dict()
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

# Convert with dict()
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

los = ['ab', 'cd', 'ef'] # two-character string
print(dict(los))

# ADDING/CHANGING ITEMS BY [Key]
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}
print(pythons)
# Adding/Updating a dict value by assignment
pythons['Gilliam'] = 'Gerry'
print(pythons)
# Updating by assignment
pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones'
}
print(some_pythons)

# Get an item by [key] or with get()
print(some_pythons['John'])
print(some_pythons['Groucho'])
print(some_pythons.get('John'))
print(some_pythons.get("Groucho", "Not a Python"))  # will print 'Not a Python' since key doesn't exist in dict
print(some_pythons.get("Groucho")) # default error value of None will be printed if element doesn't exist in dict

# GET ALL KEYS FROM A DICTIONARY USING keys()
signal = {'green':'go', 'yellow':'go faster', 'red':'smile for the camera'}
print(signal.keys())
print(list(signals.keys()))

# All values
print(signal.values())
print(list(signal.values()))

# Both values and keys
print(list(signal.items())) # returns value as a tuple as default

# length with len()
print(len(signal))

# MERGE DICTIONARIES
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
merged_dict = {**first, **second}
print(merged_dict)
third = {'d': 'donuts'}
merged_dict = {**first, **third, **second}
print(merged_dict)

# Merging dictionaries with update()
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}
others = {"Marx": "Groucho", "Howard": "Moe"}
pythons.update(others)
print(pythons)

# if both dicts have the same key, the second dict values overwrite those of the first
first = {"a": 1, "b": 2}
second = {"b": "platypus"}
first.update(second)
print(first)

# Delete with del()
del pythons["Marx"]
print(pythons)
del pythons['Howard']
print(pythons)

# DELETE WITH pop()
print(len(pythons))
forgotten = {"Gilliam": "Terry"}
pythons.update(forgotten)
print(pythons)
print(pythons.pop("Palin"))
print(pythons)
print(pythons.pop("Palin")) # will generate an exception

print(pythons.pop('first', 'Hugo'))  # if second argument is given to pop, the dict remains the same
print(len(pythons))

# DELETE EVERYTHING WITH clear() or assign dict to empty dict
pythons.clear()
print(pythons)

# COMPARE DICTIONARIES
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b)

a = {1: [1, 2], 2: [1], 3:[1]}
b = {1: [1, 1], 2: [1], 3:[1]}
print(a == b)

# ITERATE WITH FOR and  IN
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation:
    print(card) # will print keys

# to get values
for value in accusation.values():
    print(value)
    
# to return both key and value
for item in accusation.items():
    print(item)
    
# Assign keys and values to tuples
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
    
# DICTIONARY COMPREHENSION
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
# more pythonic way
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# for and if clauses in dict comprehensions
vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) 
                if letter in vowels}
print(vowel_counts)

# JUMPING TO LAMBDA, MAP, FILTER AND REDUCE()
# lambda & map()
# a = [1, 2, 3]
# b = [17, 12, 11, 10]
# c = [-1, -4, 5, 9]

# print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))

# filter
# fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# odd_numbers = list(filter(lambda x: x % 2, fibonacci))
# even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
# print(odd_numbers)
# print(even_numbers)

# extended version
# for number in fibonacci:
#     if number % 2 == 1:
#         print(number, end=" ")

# REDUCE
# import functools
# print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4]))

#finding the max number in a list using reduce
# from functools import reduce
# f = lambda a, b : a if (a > b) else b
# print(reduce(f, [47, 11, 42, 102, 13]))

# calculating the sum of numbers from 1 to 100
# print(reduce(lambda x, y: x+y, range(1, 101)))

# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = 0
# new_list = set(my_list)
# for item in new_list:
#     result +=  item
# print(result)

# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# print(set_1 & set_2)

# a_dict = {"language": "C", "number": 13, "track": "Low_level"}
# count = 0
# for key in a_dict.keys():
#     count += 1
# print(count)

# a_dict = {"language": "C", "number": [3, 1, 2], "track": "Low_level"}
# for keys in sorted(a_dict.keys()):
#     print("{}: {}".format(keys, a_dict[keys]))
