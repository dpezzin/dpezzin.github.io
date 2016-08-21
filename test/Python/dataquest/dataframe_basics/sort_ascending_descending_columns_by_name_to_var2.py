#!/usr/bin/env python
# Sort foods by amount of fat.
# The first argument to the sort method is a list of columns to sort by.
# For now, we are only sorting by a single column, so there is only one argument.
# The other argument is named, and specifies the sort order of each of the columns.  True means the columns should be ascending (smallest value first, then increase)
# False means that they should be descending (largest value first, then decrease)
descending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[False])

# Print the most fatty food in the data.
print(descending_fat.iloc[0,:])

# We can reverse the sort order.
ascending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[True])

# The least fatty food has no fat at all
print(ascending_fat.iloc[0,:])


# Sort by the amount of "Sodium_(mg)", with the largest value on top (descending sort)
# Assign the result to descending_sodium.
# Sort by the amount of "Vit_C_(mg)", with the smallest value on top (ascending sort). Assign the result to ascending_vitamin_c.
descending_sodium = food_info.sort(["Sodium_(mg)"], ascending=[False])
ascending_vitamin_c = food_info.sort(["Vit_C_(mg)"], ascending=[True])