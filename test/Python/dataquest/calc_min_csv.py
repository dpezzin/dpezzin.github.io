#!/usr/bin/env python
# We now know everything we need to find the smallest crime rate.
# Remember that we are finding the smallest crime rate (second column), not the city (first column) with the lowest crime rate.
# We parse our csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

lowest_crime_rate = 10000

# Set lowest_crime_rate equal to the lowest crime rate in full_data. 
# Use for loops and if statements like we did in the last screen. 
# You'll also need to the index the second item in each row inside the loop.
for row in full_data:
    crime_rate = row[1]
    if crime_rate < lowest_crime_rate:
        lowest_crime_rate = crime_rate