# poem = """There was a Young Lady of Norway,
# Who casually sat in a doorway;
# When the door squeezed her flat
# She exclaimed, 'What of that?'
# This courageous Young Lady of Norway."""
# print(poem)

# poem_2 = '''I do not like thee, Doctor Fell.
#     The reason why, I cannot tell.
#     But this I know, and know full well:
#     I do not like thee, Doctor Fell.
# '''
# print(poem_2)

# palindrome = 'A man, \nA plan, \nA canal: \nPanama.'
# print(palindrome)

# the r (raw string) formatting negates any type of escape
# used in a string.
# info = r'Type a \n to get a new line in a normal string'
# print(info)

# poem_3 = r'''Boys and girls, come out to play.
# The moon doth shine as bright as day.'''
# print(poem_3)

# msg = "My word! ""A gentleman caller"
# print(msg)

# duplicate with *
# start = 'Na ' * 4 + '!' + '\n'
# middle = 'Hey ' * 3 + '!' + '\n'
# end = 'Goodbye.'
# print(start + start + middle + end)

# Replacing strings
# name = "Koshe"
# print(name.replace('e', 'a'))
# print(name[:4] + 'a') # alternatives
# print('M' + name[1:]) # alternatives

# using slicing to obtain strings
# using step size
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabets[::7]) # means start from the beginning and iterate through seven letters at a time
# print(alphabets[4:20:3]) # same principle
# print(alphabets[-1::-1]) # print everything in reverse
# print(alphabets[::-1]) # alternative form of above, same result

# Testing long strings for reversability
# lithe = """I am Joshua. I like to reverse things
#             You are reading this upside down
#             Hope you like it."""
# print(lithe[::-1])

# Splitting strings
# tasks = "get gloves,get mask,give cat vitamins,call ambulance"
# print(tasks.split(','))

# Joining strings
# folk_lore = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
# flore_str = ', '.join(folk_lore)
# print('Found and signing book deals:', flore_str)

# Replacing strings
# use .replace(old, new, [number of instances to replace])

# More string methods
# Find and Index - used to search and select subset of
# strings
poem = """All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt."""
# to check if the string starts with a particular string set
# print(poem.startswith('All')) # True is yes, False if not

# ends with check
# print(poem.endswith("That's all, folks!"))

# finding strings
# word = 'the'
# the find() method returns the position of the search term if it exists, -1 if it doesn't
# it also searches from the beginning of the query string
# returning the position of the first instance of the search term
# print(poem.find(word))
# print(poem.index(word)) # an alternative to find, smae principle but raises and exception if search
# string not found instead of returning -1 

# searching from the end/stop of query string
# print(poem.rfind(word))
# print(poem.rindex(word))

# word = 'mother' # word doesn't exist in poem
# print(poem.find(word))
# print(poem.index(word)) # exception raised: ValueError: substring not found

# counting number of occurrences of a search term in a query string
# word = 'the'
# print(poem.count(word))

# check if query string contains letters and/or numbers only
print(poem.isalnum())