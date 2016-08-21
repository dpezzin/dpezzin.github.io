#!/usr/bin/env python
column_list = ["Energ_Kcal", "Protein_(g)"]

# This will loop through column_list, and normalize each of the columns in it.
for column in column_list:
    food_info[column] = food_info[column] / food_info[column].max()

# All columns is a list of all the columns in the food_info dataframe.
all_columns = list(food_info.columns.values)
print(all_columns)


# Remove the "NDB_No" and "Shrt_Desc" columns from all_columns
# Then, use a for loop to normalize all the other columns.
column_count = len(all_columns)
all_columns = all_columns[2:column_count]

for column in all_columns:
    food_info[column] = food_info[column] / food_info[column].max()