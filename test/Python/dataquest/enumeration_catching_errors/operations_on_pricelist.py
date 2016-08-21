#!/usr/bin/env python
# Define a list of lists
data = [["tiger", "lion"], ["duck", "goose"], ["cardinal", "bluebird"]]

# Extract the first column from the list
first_column = [row[0] for row in data]


# Double all of the prices in apple_price, and assign the resulting list to apple_price_doubled.
# Subtract 100 from all of the prices in apple_price, and assign the resulting list to apple_price_lowered.
apple_price = [100, 101, 102, 105]

apple_price_doubled = [price*2 for price in apple_price]
apple_price_lowered = [price-100 for price in apple_price]