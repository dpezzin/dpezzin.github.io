#!/usr/bin/env python


# make a Pmf object that represents a 6-sided die.
d6 = Pmf([1,2,3,4,5,6])
d6.normalize()
d6.name = 'one die'
print(d6)

