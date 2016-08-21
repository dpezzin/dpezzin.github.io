#!/usr/bin/env python
import matplotlib.pyplot as plt

# Make a scatter plot of X and Y fire positions
plt.scatter(forest_fires["X"], forest_fires["Y"])

# Set the x axis label
plt.xlabel('X position in grid')
# Set the y axis label
plt.ylabel('Y position in grid')
# Set the title
plt.title("Grid positions of fires in Montesinho national park")
plt.show()


# Make a scatterplot with the "wind" column on the x axis and the "area" column on the y axis.
# Give the chart the title "Wind speed vs fire area", the y axis label "Area consumed by fire", and the x axis label "Wind speed when fire started".
# Make a scatter plot of X and Y fire positions
plt.scatter(forest_fires["wind"], forest_fires["area"])

# Set the x axis label
plt.xlabel('Wind speed when fire started')
# Set the y axis label
plt.ylabel('Area consumed by fire')
# Set the title
plt.title("Wind speed vs fire area")
plt.show()
