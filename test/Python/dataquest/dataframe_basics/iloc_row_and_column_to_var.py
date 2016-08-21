#!/usr/bin/env python
# This is a series.
first_row = food_info.iloc[0,:]

# Get the first ten items in the first row.  Note how we index the series.
first_ten_items_in_first_row = first_row[0:10]

# Equivalent to the above two statements, just condensed.
first_ten_items_in_first_row = food_info.iloc[0,:][0:10]


# Assign the first 20 items in the second row to first_20_items_in_second_row.
# Assign the first 10 items in the first column to first_10_items_in_first_column.
first_20_items_in_second_row = food_info.iloc[1,:][0:20]
first_10_items_in_first_column = food_info.iloc[:,0][0:10]