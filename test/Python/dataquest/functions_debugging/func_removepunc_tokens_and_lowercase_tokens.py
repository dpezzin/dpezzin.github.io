#!/usr/bin/env python
# This is our function to remove punctuation.
def remove_punctuation(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    return token

# We've read the tokens from Julius's story into the tokenized_story variable.
# Can you add to the remove_punctuation function so it also lowercases the tokens?
# Then loop over the tokens in tokenized_story, normalize them with the function, and append them to normalized_tokens.
normalized_tokens = []

def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

# We've read the tokens from Julius's story into the tokenized_story variable.
# Can you add to the remove_punctuation function so it also lowercases the tokens?
# Then loop over the tokens in tokenized_story, normalize them with the function, and append them to normalized_tokens.
normalized_tokens = []


# The remove_punctuation function is to the right.
# Can you add to it so that it also makes the output lowercase?
# Then loop over the tokens in tokenized_story and normalize them with the function.
# Append the tokens to normalized_tokens when you're done.

for token in tokenized_story:
    token = normalize(token)
    normalized_tokens.append(token)