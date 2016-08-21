#!/usr/bin/env python
# Vectors are similar to python lists in that they can be indexed with only one number.
# Think of a vector as just a single row, or a single column.
# Countries is a vector.
countries = world_alcohol[:,2]

# We can index a vector with only one number.
print(countries[0])
print(countries[10])

# We can also slice vectors to get some of the values in the vector.
# The result is a new, smaller, vector.
# Slicing gets values from the first index up to but not including the second index.
print(countries[1:10])
print(countries[50:70])


# Assign index 30 in the years column to years_30.
# Assign from index 80 to index 200, inclusive, in the years columns to years_80_200.
# Assign from index 100 to index 103, inclusive, in the years columns to years_100_103.
years = world_alcohol[:,0]
years_30 = years[30]
years_80_200 = years[80:201]
years_100_103 = years[100:104]
