#!/usr/bin/env python
# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

# Pulls out the first element in the first list.
a = lolists[0][0]

# Pulls out the third element in the second list.
b = lolists[1][2]

# We can also directly do math with expressions.
c = lolists[0][2] + 10

# Any expression in python can be manipulated without first assigning it to a variable.
d = 10

# Set e equal to d times the first element in the third inner list of lolists
e = d * lolists[2][0]