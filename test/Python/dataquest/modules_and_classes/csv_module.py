#!/usr/bin/env python
import csv

f = open("la_weather.csv", 'r')

# We call the reader function, which is inside the csv module.
# It returns a value that we assign to csvreader.
csvreader = csv.reader(f)

# We'll get more into what the value stored in the csvreader variable is later on.
# For now, we can turn it into a list by using the list function.
# Just like int() turns a value into an integer, list() turns a value into a list.
data = list(csvreader)

# Wasn't that easy?  We read in all of the weather data from the mission before, but we did it with a lot less work.
print(data)


# Read in all of the data from "nfl.csv" into the nfl variable using the csv module.
f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl = list(csvreader)
