#!/usr/bin/env python
# At the 95% confidence interval for a two-sided t-test we must use a p-value of 0.975
pval = 0.975

# The degrees of freedom
df = pisa.shape[0] - 2

# The probability to test against
p = t.cdf(tstat, df=df)


# Do we accept β1>0? Assign the boolean value, True or False, to variable beta1_test.
beta1_test = p > pval
