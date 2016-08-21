#!/usr/bin/env python
# We can open files with the open function.
# The open function returns a file object, which we store in a variable so that we can use it later.
a = open("test.txt", "r")
print(type(a)) #type is _io.TextIOWrapper
b = open("crime_rates.csv", "r")