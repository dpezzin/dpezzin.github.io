#!/usr/bin/env python
import matplotlib.pyplot as plt

# Let's say that we want to graph weight vs height.
weight = [600,150,200,300,200,100,125,180]

# Height is in inches
height = [60,65,73,70,65,58,66,67]

# Now let's make a plot.
# The first input will be the x-axis, and the second will be the y-axis.
plt.scatter(weight, height)
plt.show()

# Let's get data on airline trip length in minutes vs cost in dollars.
airline_trip_length = [100,500,200,800,300,100]
airline_trip_cost = [200,1000,500,3000,1000,300]


# Create a scatterplot that graphs airline_trip_length on the x-axis, and airline_trip_cost on the y-axis.
plt.scatter(airline_trip_length, airline_trip_cost)
plt.show()