#!/usr/bin/env python
# Read in all of the birth data
import pandas
with open("births.csv", 'r') as f:
    births = pandas.read_csv(f)
    
# There are large differences between the first pregnancy and subsequent onces, so let's split the data up.
firsts = births[births["birthord"] == 1]
others = births[births["birthord"] > 1]

# We end up with around 7000 rows for each.
print(others.shape)
print(firsts.shape)


# Find the mean agepreg for mothers in firsts. Assign the result to mean_firsts_agepreg.
# Find the mean agepreg for mothers in others. Assign the result to mean_others_agepreg.
mean_firsts_agepreg = firsts["agepreg"].mean()
mean_others_agepreg = others["agepreg"].mean()