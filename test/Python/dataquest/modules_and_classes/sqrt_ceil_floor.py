#!/usr/bin/env python
# Let's say we want to take the square root of a number.
# Python's math module has a handy function that can do that.
# But, we have to import the module before we can use it.
import math

# Now, we can access the functions in the module by using the module name, then a dot, then the function to use.
# The sqrt function in the math module will take the square root of a number.
print(math.sqrt(9))

# We can use other functions, too.
# The ceil function will always round a number up.
print(math.ceil(8.1))

# And the floor function will always round a number down.
print(math.floor(11.9))


# Assign the square root of 16 to a.
# Assign the ceiling of 111.3 to b. (round up)
# Assign the floor of 89.9 to c. (round down)
a = math.sqrt(16)
b = math.ceil(111.3)
c = math.floor(89.9)