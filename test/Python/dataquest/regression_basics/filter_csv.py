#!/usr/bin/env python
# The data is loaded into the sp500 variable.


# Remove any rows that contain a . in the value column from the sp500 dataframe.
sp500 = sp500[sp500["value"] != "."]