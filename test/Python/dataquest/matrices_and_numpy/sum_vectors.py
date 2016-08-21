#!/usr/bin/env python
# Create a boolean vector that contains True where year is 1985 and the country is Algeria.
algeria_1985 = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == '1985')

# Subset the alcohol consumption vector with our boolean, and get the sum.
# The sum is the total amount of alcohol and average Algerian drank in 1985.
algeria_1985_alcohol = alcohol_consumption[algeria_1985].sum()


# Assign the total amount of alcohol an average person in "Canada" drank in "1986" to canada_1986_alcohol.
# Assign the total amount of alcohol an average person in "Trinidad and Tobago" drank in "1987" to trinidad_1987_alcohol.
canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986_alcohol = alcohol_consumption[canada_1986].sum()

trinidad_1987 = (world_alcohol[:,2] == "Trinidad and Tobago") & (world_alcohol[:,0] == '1987')
trinidad_1987_alcohol = alcohol_consumption[trinidad_1987].sum()