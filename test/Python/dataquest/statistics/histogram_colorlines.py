#!/usr/bin/env python
# The cleaned up data has been loaded into the titanic_survival variable
import matplotlib.pyplot as plt
import numpy


# Plot a histogram of the "age" column in titanic_survival.
# Add in a blue line for the median.
# Add in a red line for the mean.
plt.hist(titanic_survival["age"])
plt.axvline(numpy.median(titanic_survival["age"]), color="b")
plt.axvline(titanic_survival["age"].mean(), color="r")
plt.show()