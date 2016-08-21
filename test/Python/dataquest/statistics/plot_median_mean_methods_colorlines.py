#!/usr/bin/env python
# Let's plot the mean and median side by side in a negatively skewed distribution.
# Sadly, numpy arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")

# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# See how the median is further to the right than the mean?
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()


# Plot a histogram for test_scores_positive.
# Add in a blue line for the median.
# Add in a red line for the mean.
plt.hist(test_scores_positive)
plt.axvline(numpy.median(test_scores_positive), color="b")
plt.axvline(test_scores_positive.mean(), color="r")
plt.show()