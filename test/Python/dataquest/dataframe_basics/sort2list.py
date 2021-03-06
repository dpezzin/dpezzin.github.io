#!/usr/bin/env python
most_nutritious_foods = []


# Find the three most nutritious foods by sorting food_info using the "nutritional_rating" column.
# Get the name of those foods (the "Shrt_Desc" column), and assign the names to most_nutritious_foods.
# If most_nutritious_foods isn't a list at the end, use the list() function to turn it into one.
sorted_food_info = food_info.sort(["nutritional_rating"], ascending=[False])
most_nutritious_foods = sorted_food_info["Shrt_Desc"].iloc[0:3]
most_nutritious_foods = list(most_nutritious_foods)