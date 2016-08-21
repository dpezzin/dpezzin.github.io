#!/usr/bin/env python
# The columns are Year, Region, Country, Beverage type, and Number of liters of pure alcohol drunk per person
# The print function below prints the number of liters of pure alcohol vietnamese drank in wine in 1986.
print(world_alcohol[0,4])

# The Beverage type can take the values "Beer", "Wine", "Spirits", and "Other"

# If we want to grab a whole row, we replace the column number with a colon, which means "get all of the columns"
print(world_alcohol[0,:])

# If we want to grab a whole column, we do the same thing with the row number.
countries = world_alcohol[:,2]


# Assign the amount of alcohol Uruguayans drank in other beverages per capita in 1986 to uruguay_other_1986. This is the second row in the data.
# Assign the whole fourth row to row_four.
# Assign the whole year column to years.
uruguay_other_1986 = world_alcohol[1,4]
row_four = world_alcohol[3,:]
years = world_alcohol[:,0]
