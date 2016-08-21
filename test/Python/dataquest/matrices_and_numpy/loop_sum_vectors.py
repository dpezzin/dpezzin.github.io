#!/usr/bin/env python
# country_consumption_1989 has been loaded in for you.
lowest_country = None
lowest_consumption = None


# Loop over the keys in country_consumption_1989 and find the country where the average person drank the least in 1989.
# To do this, you'll need to use a for loop, and keep track of the lowest value and country.
# Assign the lowest value to lowest_consumption, and the country with the lowest value to lowest_country.
for country in country_consumption_1989:
    consumption = country_consumption_1989[country]
    if lowest_consumption is None or lowest_consumption > consumption:
        lowest_consumption = consumption
        lowest_country = country