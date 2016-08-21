#!/usr/bin/env python
# The "days" column in our data isn't extremely useful for our task, so we need to just grab the second column, with the weather.
# We looped over lists before, and this is how we will extract the second column.
lolist = [[1,2],[3,4],[5,6],[7,8]]
second_column = []
for item in lolist:
    # Each item in lolist is a list.
    # We can get just the second column value by indexing the item.
    value = item[1]
    second_column.append(value)

# second_column is now a list containing only values from the second column of lolist.
print(second_column)

# Let's read in our weather data again.
weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)

	
# Get all of the values in the second column and append them to weather_column.
weather_column = []

for row in weather_data:
    weather_column.append(row[1])