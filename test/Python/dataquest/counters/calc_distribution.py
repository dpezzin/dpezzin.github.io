#!/usr/bin/env python


# make a Pmf object that represents a 6-sided die.
d6 = Pmf([1,2,3,4,5,6])
d6.normalize()
d6.name = 'one die'
print(d6)

# Using the add operator, we can compute the distribution for the sum of two dice.
d6_twice = d6 + d6
d6_twice.name = 'two dice'

for key, prob in d6_twice.items():
    print(key, prob)
