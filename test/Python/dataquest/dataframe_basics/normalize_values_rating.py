#!/usr/bin/env python
better_protein_rating = None


# Superman is twice as interested in a food having a lot of protein than he is in it having too much fat.
# Construct a rating with these new criteria, and assign it to better_protein_rating.
# Make sure to normalize the protein ("Protein_(g)") and fat ("Lipid_Tot_(g)") columns first!
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

better_protein_rating = (normalized_protein * 2) - normalized_fat