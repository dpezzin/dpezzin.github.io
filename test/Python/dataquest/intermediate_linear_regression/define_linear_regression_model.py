#!/usr/bin/env python
# Our predicted values of y
yhat = linearfit.predict(X)
print(yhat)


# Using linearfit with data X and y predict the residuals. 
# Residuals are computed by subtracting the observed values from the predicted values. 
# Assign the residuals to variable residuals.
residuals = yhat - y
