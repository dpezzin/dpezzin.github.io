#!/usr/bin/env python
# We can check if values are in lists using the in statement.
the_list = [10,60,-5,8]

# This is True because 10 is in the_list
print(10 in the_list)

# This is True because -5 is in the_list
print(-5 in the_list)

# This is False because 9 isn't in the_list
print(9 in the_list)

# We can assign the results of an in statement to a variable.
# Just like any other boolean.
a = 7 in the_list

# Check if 9 is in list2, and assign the result to c. 
# Check if 8 is in list2, and assign the result to d. 
# Check if -1 is in list2, and assign the result to e.
list2 = [8, 5.6, 70, 800]
c = 9 in list2
d = 8 in list2
e = -1 in list2