#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy
# The pivot_table method will return a new array containing a summary of the data.
# This pivot table will have the Y position of the fire as the index, and the average area of forest burned per fire as the values.
# It will return a vector, or one dimensional array.
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)

# This gets the index values of the vector, in this case, the sorted y positions
y_index = area_by_y.index
plt.bar(y_index, area_by_y)
plt.show()


# Make a bar plot with "X" on the x axis, and "area" on the y axis.
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
plt.bar(area_by_x.index, area_by_x)
plt.show()