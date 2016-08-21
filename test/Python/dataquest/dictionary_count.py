#!/usr/bin/env python
# We can count how many times items appear in a list using dictionaries.
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

# Create an empty dictionary
pantry_counts = {}
# Loop through the whole list
for item in pantry:
    # If the list item is already a key in the dictionary, then add 1 to the value of that key.
    # This is because we've seen the item again, so our count goes up.
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        # If the item isn't already a key in the count dictionary, then add the key, and set the value to 1.
        # We set the value to 1 because we are seeing the item, so it's occured once already in the list.
        pantry_counts[item] = 1
print(pantry_counts)


# Count how many times each presidential last name appears in us_presidents. Assign the #counts to us_president_counts.
us_presidents = ["Adams", "Bush", "Clinton", "Obama", "Harrison", "Taft", "Bush", "Adams", "Wilson", "Roosevelt", "Roosevelt"]

us_president_counts = {}

for president in us_presidents:
    if president in us_president_counts:
        us_president_counts[president] = us_president_counts[president] + 1
    else:
        us_president_counts[president] = 1