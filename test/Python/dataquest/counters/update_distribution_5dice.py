#!/usr/bin/env python


# use the list of dice to instantiate a Suite that 
# maps from each die to its prior probability. 
# By default, all dice have the same prior.

# Then I update the distribution with the given value and print the results:
dice_suite = DiceSuite(dice)

dice_suite.bayesian_update(6)

for die, prob in dice_suite.items():
    print(die.name)
    print(prob)