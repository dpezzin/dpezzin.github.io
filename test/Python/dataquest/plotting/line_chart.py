#!/usr/bin/env python
import matplotlib.pyplot as plt
# We can use the plt.plot() function to make a line plot.
plt.plot(forest_fires["temp"], forest_fires["area"])
plt.show()

# Hmm, the above plot looks really strange (check in the plots area to look for yourself)
# The reason it does is because we didn't sort based on the x-axis variable first.
# If we don't sort, points are placed wherever they occur in the data, which means lines can be drawn all across the figure.
# Sorting puts all of the values in the order of the x axis, which means a line is drawn from left to right.
forest_fires = forest_fires.sort(["temp"])
plt.plot(forest_fires["temp"], forest_fires["area"])
plt.show()

# The above plot looks much better!


# Plot "rain" on the x axis and "area" on the y axis.
# Plot "wind" on the x axis and "area" on the y axis.
# Remember to sort on the x-axis values first!
forest_fires = forest_fires.sort(["rain"])
plt.plot(forest_fires["rain"], forest_fires["area"])
plt.show()
forest_fires = forest_fires.sort(["wind"])
plt.plot(forest_fires["wind"], forest_fires["area"])
plt.show()