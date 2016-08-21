#!/usr/bin/env python
max_val = None
data = [-10, -20, -50, -100]
for i in data:
    # If max_val equals None, or i is greater than max_val, then set max_val equal to i.
    # This ensures that no matter how small the values in data are, max_val will always get changed to a value in the list.
    # If you are checking if a value equals None and you are using it with and or or, then the None check always needs to come first.
    if max_val is None or i > max_val:
        max_val = i

		
# Use a for loop to set min_val equal to the smallest value in income.
min_val = None
income = [100,700,100,50,100,40,56,31,765,1200,1400,32,6412,987]
for i in income:
    if min_val is None or i < min_val:
        min_val = i