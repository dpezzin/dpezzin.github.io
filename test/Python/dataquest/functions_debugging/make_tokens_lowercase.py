#!/usr/bin/env python
# We can make strings all lowercase using the .lower() method.
text = "MY CAPS LOCK IS STUCK"
text = text.lower()

# The text is much nicer to read now.
print(text)

# The tokens without punctuation have been loaded into no_punctuation_tokens.
# Loop through the tokens and lowercase each one.
# Append each token to lowercase_tokens when you're done lowercasing.
lowercase_tokens = []

for token in no_punctuation_tokens:
    token = token.lower()
    lowercase_tokens.append(token)