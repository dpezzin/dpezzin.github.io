#!/usr/bin/env python
lolist = [[1,5,7],[10,8,9],[7,10,11]]

# Let's say we want to get the first element of the inner list whose third element is 9.
value = 0
for item in lolist:
    last_value = item[2]
    first_value = item[0]
    if last_value == 9:
        value = first_value
print(value)

# The above code will print 10, which is the first value in the inner list where 9 is the last value.
# What we are doing can also be described in terms of rows and columns.
# We are finding the first column in the rows where the third column equals 9.

# Can you write code to find the second element in the inner list whose first element is 7? (search through lolist)
# Set the value variable equal to the answer.
value = 0

# Find the second element in the inner list whose first element is 7. You'll need to search through lolist to do it. 
# Assign the answer to the value variable.
for item in lolist:
    if item[0] == 7:
        value = item[1]