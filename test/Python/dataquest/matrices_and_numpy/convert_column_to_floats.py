#!/usr/bin/env python
bad_value = ''
alcohol_consumption_float_column = None


# Replace all the values in the alcohol consumption column (column 5) that equal bad_value with '0'.
# Then convert all of the values in the column to floats, and assign the result to alcohol_consumption_float_column.
# At the end, alcohol_consumption_float_column should contain a column of floats.
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption[alcohol_consumption == bad_value] = '0'
alcohol_consumption_float_column = alcohol_consumption.astype(float)