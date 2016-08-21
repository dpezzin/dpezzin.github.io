#!/usr/bin/env python
import matplotlib.pyplot as plt

# Print all available styles
print(plt.style.available)

# Use the ggplot style for plotting
plt.style.use('ggplot')

plt.scatter(forest_fires["wind"], forest_fires["area"])
# This plot looks a lot better!
plt.show()


# Switch to the "fivethirtyeight" style.
# Plot "rain" on the x axis and "area" on the y axis.
plt.style.use('fivethirtyeight')

plt.scatter(forest_fires["rain"], forest_fires["area"])
plt.show()
