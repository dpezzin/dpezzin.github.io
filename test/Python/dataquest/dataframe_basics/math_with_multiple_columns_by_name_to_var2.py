#!/usr/bin/env python
# Divide the protein column by a scalar to get kilograms.
protein_kilograms = food_info["Protein_(g)"] / 1000

# Subtract 5 grams from carbohydrates.
lowered_carbs = food_info["Carbohydrt_(g)"] - 5


# Assign the number of grams of "Sodium_(mg)" to the variable sodium_grams (divide the column by 1000).
# Assign the number of milligrams of "Sugar_Tot_(g)" to the variable sugar_milligrams (multiply the column by 1000).
sodium_grams = food_info["Sodium_(mg)"] / 1000
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000