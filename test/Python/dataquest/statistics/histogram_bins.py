#!/usr/bin/env python
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()

# As you can see, the values in the list are counted into the nearest bin.
# If we have less bins, each bin will have a higher count (because it's showing all of the values that fall into it)
# With more bins, the counts are less, because each bin contains less values.
plt.hist(average_speed, bins=4)
plt.show()


# Plot a histogram of average_speed with only 2 bins.
plt.hist(average_speed, bins=2)
plt.show()
