# number = 1000
# a = number % 10
# if a == 0:
#     print(f"{a} is zero")
# else:
#     print(f"{a} is negative")

# for i in range(0, 10):
#     for j in range(i, 10):
#         print(i, j, end="")

# #!/usr/bin/python3
# for first_num in range(10):
#     for second_num in range(10):
#         if first_num < second_num:
#             print("{:01d}{:01d}".format(first_num, second_num), end=", "
#             if first_num < 8 or second_num < 9 else "\n")

#!/usr/bin/python3
# def uppercase(str):
#     result = ""
#     for char in str:
#         if ord('a') <= ord(char) <= ord('z'):
#             result += chr(ord(char) - ord('a') + ord('A'))
#         else:
#             result += char
#     print(result, end='\n')

#!/usr/bin/python3
# def print_last_digit(number):
#     last_digit = abs(number) % 10
#     print("{}".format(last_digit), end="")

#!/usr/bin/python3
# def print_last_digit(number):
#     last_digit = (number % 10) if number >= 0 else (abs(number) % 10)
#     print(last_digit, end="")
    
#     return last_digit

#!/usr/bin/python3
# def add(a, b):
#     return a + b

# def pow(a, b):
#     return a ** b

# def fizzbuzz():
#     for number in range(1, 101):
#         if number % 15 == 0:
#             print("fizzbuzz", end=" ")
#         elif number % 3 == 0:
#             print("Fizz", end=" ")
#         elif number % 5 == 0:
#             print("Buzz", end=" ")
#         else:
#             print(number, end=" ")

# fizzbuzz()

# print alphabets in reverse and intermix with uppercase
#!/usr/bin/python3
# for i in range(ord('z'), ord('a') - 1, -1):
#     if i % 2 == 0:
#         print(chr(i), end="")
#     else:
#         print(chr(i - 32), end="")

# print("".join([chr(i) if i % 2 == 0 else chr(i - 32) for i in range(ord('z'), ord('a') - 1, -1)]), end="")

# def magic_calculation(a, b, c):
#     if a < b:
#         return c
#     elif c > b:
#         return a + b
#     else:
#         return a * b - c

#def remove_char_at(str, n):
#    new_str = ""
#    i = 0
#    for char in str:
#        if i != n:
#            new_str += char
#        i += 1
#    return new_str

