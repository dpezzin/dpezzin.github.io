#!/usr/bin/env python
nutritional_rating = None


# Give the "vitamin_totals" column a weight of 3, 
# the "Lipid_Tot_(g)" column a weight of -2, 
# the "Protein_(g)" column a weight of 3, 
# the "Sugar_Tot_(g)" column a weight of -1, 
# the "Fiber_TD_(g)" a weight of 1, 
# and the "Cholestrl_(mg)" column a weight of -2.
# Construct a rating using the above weights, and assign it to nutritional_rating.
nutritional_rating = 3 * food_info["vitamin_totals"] + -2 * food_info["Lipid_Tot_(g)"] + 3 * food_info["Protein_(g)"] + -1 * food_info["Sugar_Tot_(g)"] + 1 * food_info["Fiber_TD_(g)"] + -2 * food_info["Cholestrl_(mg)"]