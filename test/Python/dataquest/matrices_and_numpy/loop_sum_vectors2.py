#!/usr/bin/env python
# country_consumption_1989 has been loaded in for you.
highest_country = None
highest_consumption = None


# Loop over the keys in country_consumption_1989 and find the country where the average person drank the most in 1989.
# To do this, you'll need to use a for loop, and keep track of the highest value and country.
# Assign the highest value to highest_consumption, and the country with the highest value to highest_country.
for country in country_consumption_1989:
    consumption = country_consumption_1989[country]
    if highest_consumption is None or highest_consumption < consumption:
        highest_consumption = consumption
        highest_country = country
