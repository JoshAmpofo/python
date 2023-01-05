#***Repeat with while***
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

#***Cancelling with break***
# while True:
#     text = input("String to capitalize [type q to quit]: ")
#     if text == 'q':
#         break
#     print(text.capitalize())

#***Skip ahead with continue***
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
    