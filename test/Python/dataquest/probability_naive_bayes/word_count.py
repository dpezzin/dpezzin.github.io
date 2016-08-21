#!/usr/bin/env python
# A nice python class that lets you count how many times items occur in a list
from collections import Counter
import csv
import re


# count up how many times each word occurs in the negative reviews, and how many times 
# each word occurs in the positive reviews. 
# This will allow us to eventually compute the probabilities of a new review belonging to each class.
# Read in the training data.
with open("train.csv", 'r') as file:
    reviews = list(csv.reader(file))

def get_text(reviews, score):
    # Join together the text in the reviews for a particular tone.
    # We lowercase to avoid "Not" and "not" being seen as different words, for example.
    return " ".join([r[0].lower() for r in reviews if r[1] == str(score)])

def count_text(text):
    # Split text into words based on whitespace.  Simple but effective.
    words = re.split("\s+", text)
    # Count up the occurence of each word.
    return Counter(words)

negative_text = get_text(reviews, -1)
positive_text = get_text(reviews, 1)
# Generate word counts for negative tone.
negative_counts = count_text(negative_text)
# Generate word counts for positive tone.
positive_counts = count_text(positive_text)

print("Negative text sample: {0}".format(negative_text[:100]))
print("Positive text sample: {0}".format(positive_text[:100]))