#!/usr/bin/env python
# We just counted the number of rows.  We can do the same for the number of columns.
# Let's create a list of lists, and assume that the inner lists are the rows.
# If this is the case, the number of columns is the number of items in any row.
l = [[1,2,3],[3,4,5],[5,6,7]]
first_row = l[0]
count = 0
for column in first_row:
    count = count + 1

# Count is now equal to 3, the number of items in the first row of data.
# All of the rows have the same number of items, so 3 is our column count.

# We parse our csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
   
# Set count equal to the number of columns in full_data.
first_row = full_data[0]
count = 0
for column in first_row:
    count = count + 1