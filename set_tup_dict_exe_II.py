# Make an Englist-to-French dictionary called e2f and print it
# Here are ther starter words: 'dog is chien', 'cat is chat',
# 'walrus is morse'
# e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# print(e2f)

# print the word for walrus
# print(e2f['walrus'])

# Make a French-to-English dictionary called f2e from e2f
# f2e = {v: k for k, v in e2f.items()}
# print(f2e)

# Print the English equivalent of the French word chien
# print(f2e['chien']) 

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