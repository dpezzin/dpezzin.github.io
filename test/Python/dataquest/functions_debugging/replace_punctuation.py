#!/usr/bin/env python
# In order to spell check our words, we'll be comparing the words in the story to a dictionary.
# If the word is in the dictionary, it will be correct.
# If it isn't, it will be incorrect.
# Simple, but it will be effective in this situation.
# In order to ensure that words that have apostrophes, commas, or other punctuation 
# don't get falsely marked as incorrect, we need to remove all punctuation.
# We can use the .replace function to replace punctuation in a string.
text = "Who really shot John F. Kennedy?"
text = text.replace("?", "?!")

# The question mark has been replaced with ?!.
print(text)

# We can replace strings with blank spaces, meaning that they are just removed.
text = text.replace("?", "")

# The question mark is gone now.
print(text)

no_punctuation_tokens = []

# The story has been loaded into tokenized_story.
# Replace all of the punctuation in each of the tokens.
# You'll need to loop through tokenized_story to do so.
# You'll need to use multiple replace statements, one for each punctuation character to replace.
# Append the token to no_punctuation_tokens once you are done replacing characters.
# Don't forget to remove newlines!
# Print out no_punctuation_tokens if you want to see which types of punctuation are still in the data.

for token in tokenized_story:
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    no_punctuation_tokens.append(token)