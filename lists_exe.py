# Exercise 1 - 3
# years_list = [1992, 1993, 1994, 1995, 1996]
# print(f"My third birthday was in {years_list[2]}")
# print(f"I was the oldest in {years_list[-1]}")

# Exercise 4: Capitalize the element in "things" that refers
# to a person and then print the list
# things = ['mozzarella', 'cinderella', 'salmonella']
# for thing in things:
#     if thing.startswith('c'):
#         things[1] = thing.capitalize()
# print(things)

# Exercise 5: Make the cheesy element of "things" all uppercase
# and then print the list
# for thing in things:
    # if thing.startswith('m'):
        # things[0] = thing.upper()
# print(things)

# Exercise 6: Delete the disease element from "things",
# collect your Nobel Prize, and print the list
# del things[-1]
# print(things)

# Exercise 7: Create a list called "surprise" with the
# elements "Groucho", "Chico", and "Harpo"
# surprise = list(('Groucho', 'Chico', 'Harpo'))

# Exercise 8: Lowercase the last element of the surprise list
# reverse it, and then capitalize it
# for name in surprise:
    # if name.startswith('H'):
        # surprise[-1] = name.lower()
# print(surprise)
        # surprise[-1] = name[::-1]
# print(surprise)
        # surprise[-1] = name.capitalize()
# print(surprise)

# Exercise 9: Use a list comprehension to make a list
# called even of the even numbers in range(10)
# even = [number for number in range(10) if number % 2 == 0]
# print(even)

# Exercise 100: Let's create a jump rope rhyme maker
# for the first line:
    # print each string in start1, capitalized and followed
    # by an exclamation point and a space

    # print first, also capitalized and followed by an 
    # exclamation point
#for the second line:
    # print start2 and a space
    # print second and a period.
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for (first, second) in rhymes:
    for word in start1:
        print(word.capitalize() + "! ", end="")
        print(first.capitalize() + "!")
        print(start2 + "" + second + ".")