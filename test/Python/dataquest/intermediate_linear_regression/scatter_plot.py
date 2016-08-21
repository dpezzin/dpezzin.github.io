#!/usr/bin/env python
import pandas
import matplotlib.pyplot as plt

pisa = pandas.DataFrame({"year": range(1975, 1988), 
                         "lean": [2.9642, 2.9644, 2.9656, 2.9667, 2.9673, 2.9688, 2.9696, 
                                  2.9698, 2.9713, 2.9717, 2.9725, 2.9742, 2.9757]})

print(pisa)


# Create a scatter plot with year on the x-axis and lean on the y-axis.
plt.scatter(pisa["year"], pisa["lean"])