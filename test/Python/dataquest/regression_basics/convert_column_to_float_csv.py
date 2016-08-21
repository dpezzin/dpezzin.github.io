#!/usr/bin/env python
# We can see the current types of the columns
print(sp500.dtypes)


# Convert the value and next_day columns in sp500 to be of type float.
sp500["value"] = sp500["value"].astype(float)
sp500["next_day"] = sp500["next_day"].astype(float)