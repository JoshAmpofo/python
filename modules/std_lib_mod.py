#!/usr/bin/env python3
"""Working with built in modules and packages"""

# from collections import defaultdict


#def no_idea():
#    """Return a puzzled answer"""
#    return 'Huh?'


#bestiary = defaultdict(no_idea)
#bestiary['A'] = 'Abominable Snowman'
#bestiary['B'] = 'Basilisk'

#print(bestiary['A'])
#print(bestiary['B'])
#print(bestiary['C'])


# Defining your own counter

#food_counter = defaultdict(int)
#for food in ['spam', 'spam', 'eggs', 'spam']:
#    food_counter[food] += 1

#for food, count in food_counter.items():
#    print(food, count)
####################################################################

# using the default counter()
#from collections import Counter

#family = ['Ben', 'Esther', 'Josh', 'Nat', 'Persis', 'Esther']
#family_count = Counter(family)
#print(family_count)
# most_common() returns all elements in descending order or the top count ele
#print(family_count.most_common())
#print(family_count.most_common(1))

# You can add counters together
#other_fam = ['Ben', 'Doreen', 'Esther', 'John', 'Aggie']
#other_fam_count = Counter(other_fam)
#print(other_fam_count)

# Add
#print(family_count + other_fam_count)

# subtract
#print(family_count - other_fam_count) # or vice versa

# intersection
#print(family_count & other_fam_count)

# union
#print(family_count | other_fam_count)

# OrderedDict() remebers the order of key addition and returns same order
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk, nyuk!'),
    ])

for stooges in quotes:
    print(stooges)
