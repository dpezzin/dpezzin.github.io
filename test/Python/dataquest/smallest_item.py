#!/usr/bin/env python
# We can use for loops and if statements to find the smallest value in a list.
the_list = [20,50,5,100]

# Set smallest_item to a value that is bigger than anything in the_list.
smallest_item = 1000
for item in the_list:
    # Check if each item is less than smallest_item.
    if item < smallest_item:
        # If it is, set smallest_item equal to its value.
        smallest_item = item
print(smallest_item)

# The first time through the loop above, smallest_item will be set to 20, because 20 < 1000 is True.
# The second time through, smallest_item will stay at 20, because 50 < 20 is False.
# The third time through, smallest_item will be set to 5, because 5 < 20 is True.
# The last time through, smallest_item will stay at 5, because 100 < 5 is False.

smallest_item = 1000
a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]

#Set the smallest_item variable equal to the lowest value in a. Use a for loop to loop through a.
for item in a:
    if item < smallest_item:
        smallest_item = item
print(smallest_item)