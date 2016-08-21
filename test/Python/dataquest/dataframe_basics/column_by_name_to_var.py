#!/usr/bin/env python
# First we can get the names of all the columns (in order)
print(list(food_info.columns.values))

# The we can get a column by name.
print(food_info["Protein_(g)"][0:10])

# And again.
sodium_column = food_info["Sodium_(mg)"]


# Assign the FA_Sat_(g) column to the variable saturated_fat.
# Assign the Cholestrl_(mg) to the variable cholesterol.
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]