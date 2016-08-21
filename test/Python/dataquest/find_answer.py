#!/usr/bin/env python
# We know that the lowest crime rate is 130.
# This is the second column of the data.
# We need to find the corresponding value in the first column -- the city with the lowest crime rate.

# Let's load the csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

city = ""

# Assign the city with the lowest crime rate to city.
for row in full_data:
    if row[1] == 130:
        city = row[0]