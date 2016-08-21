#!/usr/bin/env python
#Read the "crime_rates.csv" file in, split it on the newline character (\n), and store the result into the rows variable
# We can split a string into a list.
a_string = "This\nis\na\nstring\n"
split_string = a_string.split('\n')
print(split_string)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

f = open("crime_rates.csv", "r")
a = f.read()
rows = a.split('\n')