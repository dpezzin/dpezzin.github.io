#!/usr/bin/env python
# Select the first 10 values in the "type" column

# world_alcohol[:,3][beer] goes through each position in the fourth column vector (
# from 0 to the last index), and checks if the beer vector is True at the same position. 
# If the beer vector is True, it assigns the element of the fourth column at that position 
# to the subset. If the beer vector is False, the element is skipped.
types = world_alcohol[:,3][0:10]
print(types)

# Create a boolean vector that contains True or False indicating whether each element in types == "Beer"
beer_boolean = types == "Beer"
print(beer_boolean)

# Subset the types vector using the beer_boolean
# We end up with only two entries, corresponding to the entries in the types vector that have the "Beer" value
print(types[beer_boolean])


# Subset the third column of world_alcohol on whether the value is "Algeria". Assign the result to country_algeria.
# Subset the first column of world_alcohol on whether the value is "1987". Assign the result to year_1987.
country_algeria = world_alcohol[:,2][world_alcohol[:,2] == "Algeria"]
year_1987 = world_alcohol[:,0][world_alcohol[:,0] == "1987"]
print(country_algeria)
print(year_1987)