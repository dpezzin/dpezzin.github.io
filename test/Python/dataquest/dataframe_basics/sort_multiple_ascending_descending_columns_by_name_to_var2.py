#!/usr/bin/env python
# The food at the first row will be the one with the least fat.
# If there is a tie (several foods have no fat), it will be the food with 0 fat and the least sodium.
ascending_fat_then_ascending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, True])

# It's different than what we got when we just sorted on fat
print(ascending_fat_then_ascending_sodium.iloc[0,:])

# The food at the first row will be the one that has the most sodium, out of all the foods with 0 fat.
ascending_fat_then_descending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, False])

# Unsurprisingly, this is table salt
print(ascending_fat_then_descending_sodium.iloc[0,:])


# Perform a multicolumn sort on food_info, with the first column being "Sugar_Tot_(g)" ascending, and the second being "Zinc_(mg)" descending. 
# Assign the result to ascending_sugar_then_descending_zinc.

# Perform a multicolumn sort on food_info, with the first column being "Cholestrl_(mg)" descending, and the second being "Protein_(g)" ascending. 
# Assign the result to descending_cholesterol_then_ascending_protein.
ascending_sugar_then_descending_zinc = food_info.sort(["Sugar_Tot_(g)", "Zinc_(mg)"], ascending=[True, False])
descending_cholesterol_then_ascending_protein = food_info.sort(["Cholestrl_(mg)", "Protein_(g)"], ascending=[False, True])