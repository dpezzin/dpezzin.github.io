#!/usr/bin/env python
# Our weather column, minus the header, is assigned to the weather variable.
weather_counts = {}

for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1