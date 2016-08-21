#!/usr/bin/env python
# Print the shape of the world alcohol matrix.
# The first number is the number of rows, and the second is the number of columns
print(world_alcohol.shape)

# We can do the same with a vector, but they only have one dimension, so only one number is printed.
print(world_alcohol[1,:].shape)


# Assign the shape of the first column in world_alcohol to column_one_shape. The first column has index 0.
# Assign the shape of the tenth row in world_alcohol to row_ten_shape. The tenth row has index 9.
column_one_shape = world_alcohol[:,0].shape
row_ten_shape = world_alcohol[9,:].shape
