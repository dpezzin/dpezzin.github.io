#!/usr/bin/env python
# make a function to remove all punctuation
# Functions can have multiple lines in the function body.
def do_math(number):
    # Multiply the number by 10
    number = number * 10
    # Add 20 to the number
    number = number + 20
    return number

print(do_math(20))
a = do_math(10)

no_punctuation_tokens = []

# All the tokens from Julius's story are in the tokenized_story variable.
# Write a function that removes all punctuation from an input string.
# Then loop over tokenized_story and call the function to remove the punctuation from each token.
# Append the tokens to no_punctuation_tokens.

def remove_punctuation(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    return token