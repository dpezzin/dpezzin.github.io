#!/usr/bin/env python
import pandas


# Use the .head() method on a pandas dataframe to print the first 10 rows of sp500.
sp500 = pandas.read_csv("sp500.csv")

print(sp500.head(10))