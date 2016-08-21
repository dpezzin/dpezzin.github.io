#!/usr/bin/env python
lolists = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, row in enumerate(lolists):
    row.append(trees[i])

# Our list now has a new column containing the values from trees.
print(lolists)

# Legislators and birth_years have both been loaded in.


# Loop through the rows in legislators list, and append 
# the corresponding value in birth_years to each row.
for i, row in enumerate(legislators):
    row.append(birth_years[i])
    
print(birth_years)