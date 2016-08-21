#!/usr/bin/env python
# We can use the max() method to find the maximum value in a column.
max_protein = food_info["Protein_(g)"].max()

# And then we can divide the column by the scalar.
normalized_protein = food_info["Protein_(g)"] / max_protein

# See how all the values are between 0 and 1 now?
print(normalized_protein[0:20])


# Normalize the values in the "Vit_C_(mg)" column, and assign the result to normalized_vitamin_c
# Normalize the values in the "Zinc_(mg)" column, and assign the result to normalized_zinc
normalized_vitamin_c = food_info["Vit_C_(mg)"] / food_info["Vit_C_(mg)"].max()
normalized_zinc = food_info["Zinc_(mg)"] / food_info["Zinc_(mg)"].max()