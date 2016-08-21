#!/usr/bin/env python
# We need to convert the crime rate values from our csv file into integers.
# They are strings now because we originally split them up from a large string we read in.

# Here's our csv reading code from before
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    # Insert your code here.
    full_data.append(split_row)

# Insert code into the example that will turn the second value in split_row into an integer.
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)
