#!/usr/bin/env python
def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

# Read in the dictionary from the "dictionary.txt" file.
# Split it into tokens based on the space character.
# Normalize each token using the normalize function.
# Append the normalized tokens to normalized_dictionary_tokens	

normalized_dictionary_tokens = []

f = open("dictionary.txt", 'r')
tokens = f.read().split(" ")
for token in tokens:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)
