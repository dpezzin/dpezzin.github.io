#!/usr/bin/env python
import matplotlib.pyplot as plt

# This plot is short, making it platykurtic
# See how the values are distributed pretty evenly, and there isn't a huge cluster in the middle?
# Students had a wide variation in their performance
plt.hist(test_scores_platy)
plt.show()

# This plot is tall, and is leptokurtic
# Most students did very similarly to the others
plt.hist(test_scores_lepto)
plt.show()

# This plot is in between, and is mesokurtic
plt.hist(test_scores_meso)
plt.show()

# We can measure kurtosis with the kurtosis function
# Negative values indicate platykurtic distributions, positive values indicate leptokurtic distributions, and values close to 0 are mesokurtic
from scipy.stats import kurtosis


# Assign the kurtosis of test_scores_platy to kurt_platy.
# Assign the kurtosis of test_scores_lepto to kurt_lepto.
# Assign the kurtosis of test_scores_meso to kurt_meso.
kurt_platy = kurtosis(test_scores_platy)
kurt_lepto = kurtosis(test_scores_lepto)
kurt_meso = kurtosis(test_scores_meso)
