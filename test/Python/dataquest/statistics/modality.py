#!/usr/bin/env python
import matplotlib.pyplot as plt

# This plot has one mode, making it unimodal
plt.hist(test_scores_uni)
plt.show()

# This plot has two peaks, and is bimodal
# This could happen if one group of students learned the material, and one learned something else, for example.
plt.hist(test_scores_bi)
plt.show()

# More than one peak means that the plot is multimodal
# We can't easily measure the modality of a plot, like we can with kurtosis or skew.
# Often, the best way to detect multimodality is to observe the plot.


# Plot test_scores_multi, which has four peaks.
plt.hist(test_scores_multi)
plt.show()
