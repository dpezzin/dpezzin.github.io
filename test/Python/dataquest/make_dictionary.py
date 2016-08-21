#!/usr/bin/env python
# We can define dictionaries that already contain values.
# All we do is add in keys and values separated by colons.
# We have to separate pairs of keys and values with commas.
a = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}

# a is initialized with those keys and values, so we can access them.
print(a["key1"])

# Another example
b = {4: "robin", 5: "bluebird", 6: "sparrow"}
print(b[4])

# Make a dictionary c with the keys 7, 8, and 9 corresponding to the 
# values "raven", "goose", and "duck". Make a dictionary d with the 
# keys "morning", "afternoon", "evening", and "night" corresponding 
# to the values 9, 14, 19, and 23.
c = {7: "raven", 8: "goose", 9: "duck"}
print(c)
d = {"morning": 9, "afternoon": 14, "evening": 19, "night": 23}
print(d)