#!/usr/bin/env python
column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']

# Let's sum the amount of fiber and sugar in each of the foods.
row_total = food_info[column_list].sum(axis=1)

# This gives us a sum for each row in the data
print(row_total)

# Let's sum up the total amount of fiber and sugar across all the foods.
column_total = food_info[column_list].sum(axis=0)
print(column_total)

vitamin_columns = ['Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Vit_B6_(mg)', 'Vit_B12_(mcg)', 'Vit_A_IU', 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg', 'Vit_D_IU', 'Vit_K_(mcg)']


# Sum up the amount of vitamins in each food (using the vitamin_columns list to get columns 
# from the dataframe), and assign the result to vitamin_totals.
# You'll need to sum the total in each row.
vitamins = food_info[vitamin_columns]
vitamin_totals = vitamins.sum(axis=1)

# When axis is 0, it gives you a new series with the sums of all of the columns in the dataframe.
# When axis is 1, it gives you a new series with sums of all of the rows in the dataframe.