#!/usr/bin/env python
# This will get the first 10 items in the fourth column of world alcohol.
# This is the type column.
selected_types = world_alcohol[:,3][0:10]

# This will create a vector that contains True if the item at that position equal "Beer", and False if not.
# The vector is then printed.
# Note how the first three values are False, because the element in the position does not equal "Beer".
# The fourth and fifth are "True".
print(selected_types == "Beer")


# Create a vector that checks if the values in column one equal "1984". Assign the vector to years_1984.
# Create a vector that checks if the values in column three equal "Canada". Assign the vector to countries_canada.
years_1984 = world_alcohol[:,0] == "1984"
countries_canada = world_alcohol[:,2] == "Canada"