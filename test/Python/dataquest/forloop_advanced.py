#!/usr/bin/env python
# We can name the loop variable anything we want, it just has to be also used inside the loop.
the_list = [3,5,8,10,15,17,19]
sum = 0
for i in the_list:
    double_value = i * 2
    sum = sum + double_value
print(sum)

sum = 0
for each in the_list:
    triple_value = each * 3
    sum = sum + triple_value
print(sum)