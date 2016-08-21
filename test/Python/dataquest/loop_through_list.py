#!/usr/bin/env python
# We can have multiple lines underneath a for loop.
# The code above will go through the_list.
# At the end, sum will equal the sum of all of the items in the list doubled.
the_list = [3,5,8,10,15,17,19]
sum = 0
for i in the_list:
    # Double the value of i.
    double_i = i * 2
    # Add the doubled value to the sum.
    sum = sum + double_i
print(sum)

sum = 0
for i in the_list:
    triple_i = i * 3
    sum = sum + triple_i