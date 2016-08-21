#!/usr/bin/env python
# legislators has been loaded in.


# Loop through legislators, and count up how much each name where the gender column 
# equals "M" and the birth year is after 1940 occurs. Store the results in a dictionary.
# Then find the highest value in that dictionary.
# Finally, loop through the dictionary and append any keys where the value 
# equals the highest value to top_male_names.
top_male_names = []

male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] = male_name_counts[row[1]] + 1
        else:
            male_name_counts[row[1]] = 1

highest_value = None
for k,v in male_name_counts.items():
    if highest_value is None or v > highest_value:
        highest_value = v

for k,v in male_name_counts.items():
    if v == highest_value:
        top_male_names.append(k)