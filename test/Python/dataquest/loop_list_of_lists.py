#!/usr/bin/env python
# Use a for loop to print the first element of each inner list.
# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

for inner_list in lolists:
    # This will loop through and print each inner list, starting from the one at index 0.
    print(inner_list[0])