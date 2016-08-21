#!/usr/bin/env python
car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]


# Compute the mean of car_speeds and assign it to mean_car_speed.
# Compute the mean of earthquake_intensities and assign the result to mean_earthquake_intensities. 
# This value will not be meaningful, because we can't average values on a logarithmic scale this way.
mean_car_speed = sum(car_speeds) / len(car_speeds)
mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)