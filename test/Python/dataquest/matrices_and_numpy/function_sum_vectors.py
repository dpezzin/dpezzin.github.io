#!/usr/bin/env python
def calculate_consumption(country, year):
    # Fill in the rest of the function here.
    # Assume that country and year are strings.
    # You'll also need to delete the "pass" keyword.
    # The alcohol consumption column and the world_alcohol matrix are both loaded.
    pass

	
# Fill in the rest of the calculate_consumption function.
# Then use the function to calculate how much alcohol people in 
# "India" drank in "1989" on average, and store the result in india_1989_alcohol.
def calculate_consumption(country, year):
    country_year = (world_alcohol[:,2] == country) & (world_alcohol[:,0] == year)
    country_year_alcohol = alcohol_consumption[country_year].sum()
    return country_year_alcohol

india_1989_alcohol = calculate_consumption("India", "1989")