#!/usr/bin/env python
# There's one problem with our parsed CSV file -- because we parsed it from a string, all of the values are stored as strings.
# (go to the csv parsing and check types if you want to verify)
# We need the crime rate column s an integer so we can work with it.

# We can use the int() function to turn a string into an int.
# It only works with strings that have int values inside them.
a = '5'
print(type(a))

# a is a string containing the integer '5'.
# We can use the int function to parse it into the integer 5.
b = int(a)
print(b)
print(type(b))

c = '10'
d = '20'
e = '30'

#Assign the integer value of c to c_int. Assign the integer value of d to d_int. Assign the integer value of e to e_int.
c_int = int(c)
d_int = int(d)
e_int = int(e)
