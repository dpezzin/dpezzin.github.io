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


# The normalized story tokens are in normalized_story_tokens, 
# and the normalized dictionary tokens are in normalized_dictionary_tokens.
# Loop through the story tokens, and check if each token is in the dictionary.
# If the token is in normalized_dictionary_tokens, append it to correctly_spelled
# If it isn't, append it to potential_misspellings.	
potential_misspellings = []
correctly_spelled = []

for token in normalized_story_tokens:
    if token in normalized_dictionary_tokens:
        correctly_spelled.append(token)
    else:
        potential_misspellings.append(token)