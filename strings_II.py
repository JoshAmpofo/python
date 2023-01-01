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
lithe = """I am Joshua. I like to reverse things
            You are reading this upside down
            Hope you like it."""
print(lithe[::-1])