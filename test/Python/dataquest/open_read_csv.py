#!/usr/bin/env python
# We assign the file object to the variable f.
f = open("test.txt", "r")

# We can then use the .read() method on the file object to read the contents of the file.
# Objects are code constructs that have methods that can act on them.
# We'll make our own objects later on (and in fact, strings, ints, and floats are all objects that have their own special method)
a = f.read()

# We can print out a.
# a is just a string -- it has the entire contents of the file test.txt.
print(a)

f = open("crime_rates.csv", "r")
b = f.read()