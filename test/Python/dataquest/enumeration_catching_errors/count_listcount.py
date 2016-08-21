#!/usr/bin/env python
# female_name_counts has been loaded in.


# Loop through the keys in female_name_counts.
# If any value equals 2, append the key to top_female_names.
# At the end, top_female_names will be a list of the most occurring female congressperson names.
top_female_names = []

for k in female_name_counts:
    if female_name_counts[k] == 2:
        top_female_names.append(k)