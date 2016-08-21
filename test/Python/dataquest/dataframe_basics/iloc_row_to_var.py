#!/usr/bin/env python
# The food_info data has been loaded in.
# Print the first element in the first row.
print(food_info.iloc[0,0])

# Print the whole first row.
print(food_info.iloc[0,:])


# Assign the second row of food_info to the variable second_row.
# Assign the tenth row of food_info to the variable tenth_row.
second_row = food_info.iloc[1,:]
tenth_row = food_info.iloc[9,:]