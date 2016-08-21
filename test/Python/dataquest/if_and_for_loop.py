#!/usr/bin/env python
# We can 'nest' if statements inside for loops, or vice versa.
the_list = [5, 10, 15, 20]

# Let's say we want to count how many elements in the_list are greater than 10.
count = 0
for item in the_list:
    if item > 10:
        count = count + 1
print(count)

# Count equals two because item > 10 evaluated to True for 2 of the items in the_list.
# Notice how we indented the body of the if statement another 4 spaces.
# Whenever you put statements that have indented blocks inside each other, you will need to indent 4 more spaces.

a = 2

# Let's say we want to print all of the elements in the_list if a > 1.
if a > 1:
    for item in the_list:
        print(item)
# The above code will print all of the items in the_list, because a > 1 evaluates to True.

# Write a for loop that prints out all of the items in the_list that are greater than 5.
for item in the_list:
    if item > 5:
        print(item)