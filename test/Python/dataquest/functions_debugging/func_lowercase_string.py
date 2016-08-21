#!/usr/bin/env python
# A simple function that takes in a number of miles, and turns it into kilometers
def split_string(text):
    return text.split(" ")

sally = "Sally sells seashells by the seashore."
# This splits the string into a list.
print(split_string(sally))

# We can assign the output of a function to a variable.
sally_tokens = split_string(sally)

lowercase_me = "I wish I was in ALL lowercase"

# Make a function that takes a string as input and outputs a lowercase version.
# Then use it to turn the string lowercase_me to lowercase.
# Assign the result to lowercased_string.
def lowercase(text):
    return text.lower()

lowercased_string = lowercase(lowercase_me)