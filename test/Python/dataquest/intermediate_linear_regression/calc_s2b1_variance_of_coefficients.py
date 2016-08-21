#!/usr/bin/env python
# Enter your code here.


# Compute s2(β1^) for linearfit. Assign this variance to variable s2b1.

# Compute SSE
SSE = np.sum((y.values - yhat)**2)
# Compute variance in X
xvar = np.sum((pisa.year - pisa.year.mean())**2)
# Compute variance in b1 
s2b1 = (SSE / (y.shape[0] - 2)) / xvar