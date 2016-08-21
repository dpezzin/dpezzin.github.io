#!/usr/bin/env python
data = [[1,1],[0,5],[10,7]]
last_value = 0

# There are some holes in this code -- it won't work properly if the first birth year is 0, for example, but its fine for now.
# It keeps track of the last value in the column in the last_value variable.
# If it finds an item that equals 0, it replaces the value with the last value.
for row in data:
    # Check if the item is 0.
    if row[0] == 0:
        # If it is, replace it with the last value.
        row[0] = last_value
    # Set last value equal to the item -- we need to do this in order to keep track of what the previous value was, so we can use it for replacement.
    last_value = row[0]

# The 0 value in the second row, first column has been replaced with a 1.
print(data)


# Loop through legislators, and replace any values in the birth_year column that are 0 with the previous value.
last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]
