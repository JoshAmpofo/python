#!/usr/bin/env python3
""" 
Learning about Regular Expressions
"""
import re  # call regex module


# simple pattern matches
# result = re.match('You', 'Young Frankenstein')
# print(result)

# compile before matching for faster matching
# youpattern = re.compile('You')
# result = youpattern.match('Young Frankenstein')
# print(result)
#####################################################################

# find exact beginning match with match()
# source = 'Young Frankenstein'
# using the start anchor "^"
# m = re.match('^You', source)
#m = re.match('You', source)  # match starts at the beginning of source

# search for a pattern that doesn't occur at the beginning of source
# m = re.match('Frank', source)  # will return nothing
# m = re.match('^Frank', source)  # same here


# using search()
# m = re.search('Frank', source)  # finds pattern anywhere in source

# using greedy matching wildcard
#m = re.match('.*Frank', source)  # searches for any char matching even zero
# if m:  # match returns an object; do this to see what matched
#    print(m.group())

#####################################################################

# finding more than one match with findall()
source = 'Young Frankenstein'
# m = re.findall('n', source)

# finding more characters after search char
m = re.findall('n.', source)
print(m)
# print('Found', len(m), 'matches')
