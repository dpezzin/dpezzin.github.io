#!/usr/bin/env python
import matplotlib.pyplot as plt
# We're going to put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot
plt.axvline(mean_test_score)

# Now we can show the plot and clear the figure
plt.show()

# When we plot test_scores_negative, a very negatively skewed distribution, we see that the mean is pulled to the left by the small values there.
# The mean can be changed easily by very large or very small values.
# This can make it misleading with distributions that are very skewed, when we expect the mean to be the center.
plt.hist(test_scores_negative)
plt.axvline(test_scores_negative.mean())
plt.show()

# We can do the same with the positive side
# See how the very high values pull the mean to the right more than you would expect?
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()


# Compute the mean of test_scores_normal, and assign to mean_normal.
# Compute the mean of test_scores_negative, and assign to mean_negative.
# Compute the mean of test_scores_positive, and assign to mean_positive.
mean_normal = test_scores_normal.mean()
mean_negative = test_scores_negative.mean()
mean_positive = test_scores_positive.mean()