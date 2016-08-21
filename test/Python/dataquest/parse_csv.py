#!/usr/bin/env python
# Let's parse the data from the last mission as an example.
# First, we open the wait times file from the last mission.
f = open("crime_rates.csv", 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

	
# Open "la_weather.csv", parse it, and assign the result to weather_data.
weather_data = []

f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)