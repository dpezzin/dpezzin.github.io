#!/usr/bin/env python
# Let's assume that Superman is three times more interested in foods having a lot of protein than he is worried about them having too much fat.
# We can "weight" the protein number by his criteria, or multiply it by three.
# First we'll calculate the weighted value for protein.
weighted_protein = food_info["Protein_(g)"] * 3

# And now the weighted value for fat.
# We'll give fat a weight of -1, because he wants to avoid foods that have a lot of it, but he cares about foods having a lot of protein three times as much.
weighted_fat = -1 * food_info["Lipid_Tot_(g)"]

# We can construct our rating by just adding the weighted values.
initial_rating = weighted_protein + weighted_fat


# Let's say Superman now decides that the food having a lot of protein is only twice as important as the food not being too fatty.
# Construct the new rating, and assign it to new_rating
new_rating = (food_info["Protein_(g)"] * 2) - food_info["Lipid_Tot_(g)"]