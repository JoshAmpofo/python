# Personal Message: Use a variable to represent a person's
# name, and print a message to that person.
# Your message should be simple, such as, "Hello Eric,"
# would you like to learn some Python today?

name = "Joshua"
msg_body = "would you like to learn some Python today?"
message = f"Hello {name}, {msg_body}"
print(message)

# Name Cases: Use a variable to represent a person's
# name, and then print that person's name in lowerxase,
# uppercase, and title case

first_name = "Joshua"
last_name = "Yentumi"
full_name = f"{first_name} {last_name}"
lower_case = f"{full_name} in lowercase is: {full_name.lower()}"
print(lower_case)
upper_case = f"{full_name} in uppercase is: {full_name.upper()}"
print(upper_case)
title_case = f"{full_name} in titlecase is: {full_name.title()}"
print(title_case)

# Famous Quote: Find a quote from a famous person you admire
# Print the quote and name of its author. Your output should 
# look something like the following, including the 
# quotation marks:
    # Albert Einstein once said: "A person who never made
    # a mistake never tried anything new."

famous_person = "Albert Einstein"
message = "Imagination is more important than knowledge."
famous_quote = f"{famous_person} once said: \"{message}\""
print(famous_quote)

# Stripping Names: Use a variable to represent a person's
# name, and include some whitespace characters at the beginning
# and end of the name. Make sure you use each character
# combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name
# is displayed. Then print the name using each of the 
# three stripping functions, lstrip(), rstrip(), and strip()
# 
name = " Joshua Ampofo " 
print(name)
tab_name = "tab: Joshua\tAmpofo"
print(tab_name)
nextln_name = "next line: Joshua\nAmpofo"
print(nextln_name)
strip_left = f"left strip: {name.lstrip()}"
print(strip_left)
strip_right = f"right strip: {name.rstrip()}"
print(strip_right)
full_strip = f"total strip: {name.strip()}"
print(full_strip)