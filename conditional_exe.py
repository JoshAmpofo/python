# Guess a number program...non-interactive
# secret = 7
# guess = int(input("Enter a number between 1 and 10: "))
# if guess < secret:
#     print("Too low!")
# elif guess == secret:
#     print("Just right!")
# else:
#     print("Too high")

# choice program for some selcted plant products
# very basic...non-interactive
small = True
green = True

if small and green: 
    print("It's a pea")
elif small and not green: # small is true, green is false
    print("It's a cherry")
elif green and not small: # green is true, small is false
    print("It's a watermelon")
else:
    print("It's a pumpkin") # both are false
