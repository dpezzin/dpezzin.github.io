#!/usr/bin/env python
# The variable residuals is in memory


# Create a histogram with 5 bins of the residuals using matplotlib's hist() function. 
# The bins parameter allows us to define the number of bins.
plt.hist(residuals, bins=5)
plt.show()