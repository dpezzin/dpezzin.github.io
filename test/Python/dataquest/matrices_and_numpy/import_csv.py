#!/usr/bin/env python
# Importing numpy is the same as other imports.
import numpy

# We'll get our nfl filename from before.
# Note that we don't need to use the open function to open it -- numpy will take care of that.
f = "nfl.csv"

# The genfromtxt function in numpy is used to read files.
# delimiter is a named keyword argument specifying that commas separate the data fields (we have a csv file, which means comma separated values).
nfl = numpy.genfromtxt(f, delimiter=",")
print(nfl)


# Import the data in "world_alcohol.csv" into the variable world_alcohol.
g = "world_alcohol.csv"
world_alcohol = numpy.genfromtxt(g, delimiter=",")
print(world_alcohol)