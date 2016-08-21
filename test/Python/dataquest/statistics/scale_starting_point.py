#!/usr/bin/env python
fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]


# Convert the values in fahrenheit_degrees so that absolute zero is at the value 0. 
# If you think this is already the case, don't change anything. Assign the result to degrees_zero.
# Convert the values in yearly_town_population so that absolute zero is at the value 0. 
# If you think this is already the case, don't change anything. Assign the result to population_zero.
population_zero = yearly_town_population
degrees_zero = [f + 459.67 for f in fahrenheit_degrees]