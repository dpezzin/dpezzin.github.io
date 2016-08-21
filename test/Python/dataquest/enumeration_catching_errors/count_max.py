#!/usr/bin/env python
# female_name_counts has been loaded in.


# Loop through the keys in female_name_counts, and get the value associated with the key.
# Assign the value to max_value if it is larger, or if max_value is None.
# At the end of the loop, max_value will be the largest value in the dictionary.
max_value = None

for k in female_name_counts:
    if max_value is None or female_name_counts[k] > max_value:
        max_value = female_name_counts[k]
        
print(max_value)