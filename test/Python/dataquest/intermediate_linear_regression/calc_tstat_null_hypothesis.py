#!/usr/bin/env python
# The variable s2b1 is in memory.  The variance of beta_1


# Using the formula above, compute the t-statistic of β1. Assign the t-statistic to variable tstat.
tstat = linearfit.params["year"] / np.sqrt(s2b1)