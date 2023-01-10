# Strating with tuples (you can pronounce them as too-pull or tub-pull - no one cares!)
# empty_tuple = ()
# print(empty_tuple)

# or
# one_marx = 'Groucho',
# print(one_marx)
# print(type(one_marx))

# or
# marx_tuple = "Groucho", "Chico", "Harpo"
# print(marx_tuple)
# print(type(marx_tuple))

# check the difference
# one_marx = "Groucho",
# print(type(one_marx))  # this returns a tuple
# print(type("Groucho",))  # this returns a string
# print(type(("Groucho",)))  # this returns a tuple

# Multiple assignments
# marx_tuple = ("Groucho", "Chico", "Harpo")
# a, b, c = marx_tuple
# print(f"{a}\n{b}\n{c}")  # each variable takes one element respectively

# Swapping values using tuples (does not require temp variables)
# first_name, last_name = "Joshua", "Ampofo"
# first_name, last_name = last_name, first_name  # swap
# print(first_name)
# print(last_name)

# Making tuples of other data types
# name_list = ["Shelly", "Colby", "Dodge"]
# print(tuple(name_list))  # convert list to tuple

# Combine tuples using "+"
# name = ("Groucho",) + ("Chico", "Harpo")
# print(name)

# Duplicate Items with "*"
# print(("yada",) * 3)

# Comparing Tuples
# a = (7, 2)
# b = (7, 2, 9)
# print(a == b)
# print(a <= b)
# print(a < b)

# Iterating with for and in
# words = ("This", "ends", "here", "and", "now")
# for word in words:
#     print(word)

# Modifying tuples (YOU JUST CAN'T!!!)
# t1 = ('Fee', 'Fie', 'Foe')
# t2 = ('Flop',)
# print(id(t1))  # old ID

# t1 += t2
# print(id(t1))  # new ID

############ LISTS ##########
# creating lists
# empty_lists = [ ]
# print(empty_lists)
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# print(weekdays)
# big_birds = ["enu", "ostrich", "cassowary"]
# print(big_birds)
# first_names = ["Graham", "John", "Terry", "Terry", "Michael"]
# print(first_names)
# leap_years = [200, 2004, 2008]
# print(leap_years)
# randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]
# print(randomness)

# another_empty_list = list()
# print(another_empty_list)

# converting other data types to list
# tuple_list = ('My', 'tuple', 'is', 'now', 'a', 'list',)
# print(list(tuple_list))

# converting strings to single chars list
# print(list("cat"))

# creating a list of strings with split()
# talk_like_a_pirate_day = '9/19/2019'
# print(talk_like_a_pirate_day.split('/'))

# splitting when delimiter is '//'
# splitme = 'a/b//c/d///e'
# print(splitme.split('//'))

# SLICING
# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes[0:2])

# print(marxes[::2])
# print(marxes[::-2])  # start from the back and move two steps to the right
# print(marxes[::-1])  # start from the back and move 1 step to the left - this is reversal
# These slices do not modify the lis in place. To modify in place:
# marxes.reverse()  # function to use to reverse in place
# print(marxes)  # reversed list, changes value but returns None

# print(marxes[4:])
# print(marxes[-6:])

# LIST METHODS
# marxes.append('Zeppo')
# print(marxes)

# marxes.insert(2, 'Gummo')
# print(marxes)
# marxes.insert(10, "Zeppo")
# print(marxes)

# List can also be duplicated using *
# print(["word"] * 3)

# Combine lists using extend() or +
# marxes = ["Groucho", "Chico", "Harpo", "Zeppo"] 
# others = ["Gummo", "Karl"]
# marxes.extend(others)
# marxes += others  # Alternatively
# print(marxes)

# You can change the item in a list by using its offset
# marxes[2] = 'Wanda'
# print(marxes)

# Changing the values in a list using slicing
# numbers = [1, 2, 3, 4]
# numbers[1:3] = [8, 9]
# numbers[1:3] = [7, 8, 9]  # diff length can be inserted into a list
# numbers[1:3] = []
# numbers[1:3] = (98, 99, 100)
# numbers[1:3] = "wat?"
# print(numbers)

# Deleting list items wih del
# marxes = ["Groucho", "Chico", "Harpo", "Gummo", "Karl"]
# print(marxes[-1])
# del marxes[-1]
# print(marxes)

# rep_list = ["rep", "rep_2", "rep", "rep_3"]
# rep_list.remove("rep")
# print(rep_list)

# get and delete an item using pop()
# print(rep_list.pop(0))
# print(rep_list.pop())
# print(rep_list)

# Remove all items using clear()
work_quotes = ["working hard?", "Quick question!", "Number one priorities!"]
# print(work_quotes)
work_quotes.clear()
print(work_quotes)