#!/usr/bin/env python
import matplotlib.pyplot as plt
# The forest fire data has been loaded into the forest_fires variable as a pandas dataframe.
# We can plot the X column from the dataframe against the Y column.
# This will show us the spatial positions of all the fires on a 10x10 grid.
plt.scatter(forest_fires["X"], forest_fires["Y"])
plt.show()


# Plot the "wind" column on the x axis and the "area" column on the y axis.
# Plot the "temp" column on the x axis and the "area" column on the y axis.
plt.scatter(forest_fires["wind"], forest_fires["area"])
plt.show()

plt.scatter(forest_fires["temp"], forest_fires["area"])
plt.show()