#!/usr/bin/env python
# Print the models summary
#print(linearfit.summary())

#The models parameters
print("\n",linearfit.params)


# Assuming no external forces on the tower, how many meters will the tower of pisa lean in 15 years? 
# Assign the number of meters moved to variable delta.
delta = linearfit.params["year"] * 15
print(delta)