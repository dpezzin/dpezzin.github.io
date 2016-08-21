#!/usr/bin/env python
# We can use the .split method, with a comma as an input, to split a string on a comma.
# a_list is a list with 1,10,15, and 20 as elements.
a_string = "1,10,15,20"
a_list = a_string.split(",")
print(a_list)
print(type(a_list))
print(a_list[0])

# We split our csv file data into rows earlier.
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []

# split each string in the list rows and append the result to full_data. 
# At the end, full_data will be a list of lists containing the rows and columns 
# in the csv file. You'll need to use for loops.
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)