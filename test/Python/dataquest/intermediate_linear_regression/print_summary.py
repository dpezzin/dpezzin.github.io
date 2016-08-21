#!/usr/bin/env python
import statsmodels.api as sm

y = pisa.lean # target
X = pisa.year  # features
X = sm.add_constant(X)  # add a column of 1's as the constant term

# OLS -- Ordinary Least Squares Fit
linear = sm.OLS(y, X)
# fit model
linearfit = linear.fit()


# linearfit contains the fitted linear model to our data. Print the summary of the model by using the method .summary().
print(linearfit.summary())