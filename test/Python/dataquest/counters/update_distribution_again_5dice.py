#!/usr/bin/env python


# Now suppose I roll the die again and get an 8. 
# We can update the Suite again with the new data.

# Now the 6-sided die has been eliminated, the 8-sided die is most likely, 
# and there is less than a 10% chance that I am rolling a 20-sided die.
dice_suite.bayesian_update(8)

for die, prob in dice_suite.items():
    print(die.name)
    print(prob)