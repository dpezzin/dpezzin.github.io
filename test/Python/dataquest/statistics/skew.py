#!/usr/bin/env python
# Some numpy arrays are already loaded in, and we'll make some plots with them.
# The arrays contain student test scores from an exam, on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there is a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot is negatively skewed.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This is positively skewed.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way -- most of the values are in the center, and there is no long slope either way.
# Is is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew


# Assign the skew of test_scores_positive to positive_skew.
# Assign the skew of test_scores_negative to negative_skew.
# Assign the skew of test_scores_normal to no_skew.
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)