#!/usr/bin/env python
import numpy as np

# sum the (predicted - observed) squared
SSE = np.sum((yhat-y.values)**2)


# Compute the RSS and TSS for our model, linearfit, using the formulas above. 
# Assign the RSS to variable RSS and the TSS to variable TSS.

# Average y
ybar = np.mean(y.values)

# sum the (mean - predicted) squared
RSS = np.sum((ybar-yhat)**2)

# sum the (mean - observed) squared
TSS = np.sum((ybar-y.values)**2)