#!/usr/bin/env python
# We can replace values in a list with a for loop.
# All of the 0 values in the first column here will be replaced with a 5.
lolists = [[0,5,10], [5,20,30], [0,70,80]]
for row in lolists:
    if row[0] == 0:
        row[0] = 5

# We can see the new list.
print(lolists)


# Loop through the rows in legislators and replace any gender values of "" with "M".
for row in legislators:
    if row[3] == "":
        row[3] = "M"