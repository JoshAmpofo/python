# Make an Englist-to-French dictionary called e2f and print it
# Here are ther starter words: 'dog is chien', 'cat is chat',
# 'walrus is morse'
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

# print the word for walrus
print(e2f['walrus'])

# Make a French-to-English dictionary called f2e from e2f
f2e = {v: k for k, v in e2f.items()}
print(f2e)

# Print the English equivalent of the French word chien
print(f2e['chien']) 

# Make a multilevel dictionary called "life". Use these strings
# for the topmost keys: 'animals', 'plants', and 'other'.
# Make the 'animals' key refer to another dictionary with 
# the keys 'cats', 'octopi', and 'emus'. Make the 'cats'
# key refer to a list of strings with the values 'Henri',
# 'Grumpy', and 'Lucy'. Make all the other keys refer to empty 
# dictionaries
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
for key in life.keys():
    print(key) # print the top-level keys
    
# Print the keys for life['animals']
for keys in life['animals'].keys():
        print(keys)

# Print the values for life['animals']['cats']
for key, value in life['animals'].items():
        if key == 'cats':
                print(value)

# Use a dictionary comprehension to create the dictionary
# squares. Use range(10) to return the keys, and use the square
# of each key as its value

squares = {key: key ** 2 for key in range(10)}
print(squares)

# Use a set comprehension to create the set odd from the odd 
# numbers in range(10)

odd = {number for number in range(10) if number % 2 == 1}
print(odd)
print(type(odd))

#Use a generator comprehension to return the string 'Got '
# and a number for the numbers in range(10). Iterate
# through using a for loop
mygen = [number for number in range(10)]
for element in mygen:
        print(f"Got {element}")

# Use zip() to make a dictionary from the key tuple
# ('optimist', 'pessimist', 'troll') and the values tuple
# ('The glass if half full', 'The glass is half empty', 
# 'How did you get a glass?')

key = ('optimist', 'pessimist', 'troll')
value = ('The glass is half full', 'The glass is half empty','How did you get a glass?')

emos = {key: value for (key, value) in zip(key, value)}
print(emos)

# Use zip() to make a dictionary called 'movies' that
# pairs these lists: titles = ['Creature of Habit', 
# 'Crewel Fate', Sharks On a Plane'] and plots = ['A nun turns
# into a monster', 'A haunted yarn shop', 'Check your exits']

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop',
         'Check your exits'] 

movies = {key: value for [key, value] in zip(titles, plots)}
print(movies)