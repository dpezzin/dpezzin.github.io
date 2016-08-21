#!/usr/bin/env python
# Let's practice with some list slicing.
a = [4,5,6,7,8]
# New list containing index 2 and 3.
print(a[2:4])
# New list with no elements.
print(a[2:2])
# New list containing only index 2.
print(a[2:3])


# Assign a slice containing index 2 and 3 from slice_me to slice1. 
# Assign a slice containing index 1 from slice_me to slice2. 
# Assign a slice containing index 3 and 4 from slice_me to slice3.
slice_me = [7,6,4,5,6]

slice1 = slice_me[2:4]
slice2 = slice_me[1:2]
slice3 = slice_me[3:5]