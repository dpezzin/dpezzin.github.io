#!/usr/bin/env python
import numpy

f = "nfl.csv"
# Using the dtype keyword argument with the str type tells numpy that everything we are reading in is a string.

# "U75" tells numpy to load the file as strings.
# The "U" refers to unicode (a type of string), and the 75 is the maximum length of a string element in the data.

# While we're at it, let's also skip the header.
# We can add the optional skip_header keyword argument, and set it equal to the number of header rows to skip (1).
nfl = numpy.genfromtxt(f, delimiter=",", dtype="U75", skip_header=1)


# Read in the "world_alcohol.csv" data to world_alcohol, using the str datatype.
# Be sure to skip the header row.
f = "world_alcohol.csv"
world_alcohol = numpy.genfromtxt(f, delimiter=",", dtype="U75", skip_header=1)