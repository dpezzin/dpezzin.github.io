#!/usr/bin/env python
# This will get just the fiber and sugar columns from the data.
column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']
fiber_and_sugar = food_info[column_list]


# Assign the 'Zinc_(mg)' and 'Copper_(mg)' columns to zinc_and_copper.
# Assign the 'Selenium_(mcg)' and 'Thiamin_(mg)' columns to selenium_and_thiamin.
# Make sure that you get the columns in order (zinc and selenium come first).
zinc_and_copper = food_info[['Zinc_(mg)', 'Copper_(mg)']]
selenium_and_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]