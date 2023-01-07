# Sloop through this list and print the values
li_tem = [3, 2, 1, 0]
for item in li_tem:
    print(item)

# second
guess_me = 7
number = 1

while True:
    if number == guess_me:
        print("found it!")
        break
    elif number < guess_me:
        print("too low")
    else:
        print("oops")
        break
    number += 1

# third
guess_me = 5
for number in range(10):
    if number == guess_me:
        print("found it!", number)
        break
    elif number < guess_me:
        print("too low", number)
    else:
        print("oops!", number)
        break