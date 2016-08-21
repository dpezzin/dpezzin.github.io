#!/usr/bin/env python
# Set a variable equal to the None type
a = None
# A normal variable
b = 1

# This is True
print(a is None)
# And this is False
print(b is None)

# a is of the None type
print(type(a))

# Assigns whether a equals None to a_none
a_none = a is None
# Evaluates to True
print(a_none)

c = None
d = "Bamboo"


# Check whether c equals None, and assign the result to c_none.
# Check whether d equals None, and assign the result to d_none.
c_none = c is None
d_none = d is None