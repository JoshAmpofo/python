# Test Run
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

# Playing with the walrus :=
# the walrus allows you to combine two statements into
# a single line of code
tweet_limit = 280
tweet_string = "Blah" * 50
print(len(tweet_string))
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
# the walrus has the syntax - name := expression

# Expanded version of the code above
tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))