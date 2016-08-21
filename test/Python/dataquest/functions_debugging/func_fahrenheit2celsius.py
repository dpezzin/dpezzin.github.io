#!/usr/bin/env python
# A simple function that takes in a number of miles, and turns it into kilometers
# The input at position 0 will be put into the miles variable.
def miles_to_km(miles):
    # return is a special keyword that indicates that the function will output whatever comes after it.
    return miles/0.62137

# Returns the number of kilometers equivalent to one mile
print(miles_to_km(1))

# Convert a from 10 miles to kilometers
a = 10
a = miles_to_km(a)

# We can convert and assign to a different variable
b = 50
c = miles_to_km(b)


# Define a function that takes degrees in fahrenheit as an input, and return degrees celsius
# Use it to convert 100 degrees fahrenheit to celsius. Assign the result to celsius_100.
# Use it to convert 150 degrees fahrenheit to celsius. Assign the result to celsius_150.
fahrenheit = 80
celsius = (fahrenheit - 32)/1.8

def convert(degrees):
    return (degrees - 32)/1.8
celsius_100 = convert(100)
celsius_150 = convert(150)