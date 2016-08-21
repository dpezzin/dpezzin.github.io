#!/usr/bin/env python
day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt


# Make a line plot with day_numbers on the x axis and snail_crawl_length on the y axis.
# Make a line plot with day_numbers on the x axis and cars_in_parking_lot on the y axis.
plt.plot(day_numbers, snail_crawl_length)
plt.show()

plt.plot(day_numbers, cars_in_parking_lot)
plt.show()