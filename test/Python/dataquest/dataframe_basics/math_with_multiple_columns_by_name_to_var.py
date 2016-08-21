#!/usr/bin/env python
# Adding up all of the fat columns.
total_fat = food_info["FA_Sat_(g)"] + food_info["FA_Mono_(g)"] + food_info["FA_Poly_(g)"]

# We can also divide.
grams_of_protein_per_calorie = food_info["Protein_(g)"] / food_info["Energ_Kcal"]

# We can also multiply
grams_of_protein_squared = food_info["Protein_(g)"] * food_info["Protein_(g)"]

# And subtract
non_sugar_carbs = food_info["Carbohydrt_(g)"] - food_info["Sugar_Tot_(g)"]


# Assign the number of grams of protein per gram of water ("Protein_(g)" column divided by "Water_(g)" column) to grams_of_protein_per_gram_of_water.
# Assign the total amount of calcium and iron("Calcium_(mg)" column plus "Iron_(mg)" column) to milligrams_of_calcium_and_iron.
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]