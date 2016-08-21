#!/usr/bin/env python
# Remember how we counted the length of our list before?
# When the loop finishes, count will be equal to 5, which is the number of items in the_list.
# This is because 1 will be added to count for every iteration of the loop.
the_list = [5,6,10,13,17]
count = 0
for item in the_list:
    count = count + 1

# We can parse our csv file like we did before.
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

# Set count equal to the number of rows in full_data. You'll need to use a for loop.
count = 0
for row in full_data:
    count = count + 1