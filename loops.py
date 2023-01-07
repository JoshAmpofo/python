# ***Repeat with while***
count = 1
while count <= 5:
    print(count)
    count += 1

# ***Cancelling with break***
while True:
    text = input("String to capitalize [type q to quit]: ")
    if text == 'q':
        break
    print(text.capitalize())

# ***Skip ahead with continue***
# this is a simple program that squares an input if odd
# returns an appropriate message if even and continues to run

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0: # even number
        print("Number is even, not what we want!")
        continue
    print(f"{number} squared is {number**2}")
    
# Check break Use with else
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number", number)
        break
    position += 1
else:  # break not called
    print("No even number found")

# Iterating through strings
word = "thud"
# approach 1
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

# approach 2 (more pythonic)
for letters in word:
    print(letters)  # string iteration produces one char at a time

# breaking
word = "thud"
for letter in word:
    if letter == 'u':
        break
    print(letter)
# continue is same as in while()

# checking break Use with else
word = "thud"
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break 
    print(letter)
else:
    print("No 'x' in there")

# RANGE
for x in range(0, 3):
    print(x)

print(list(range(0, 3)))

# printing/counting backwards
for x in range(2, -1, -1):
    print(x)

print(list(range(2, -1, -1)))

print(list(range(0, 11, 2)))
