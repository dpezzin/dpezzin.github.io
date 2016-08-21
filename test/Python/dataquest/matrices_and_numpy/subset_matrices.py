#!/usr/bin/env python
# wine_rows now contains only rows where the beverage type is wine.
wine = world_alcohol[:,3] == "Wine"
wine_rows = world_alcohol[wine,:]

# wine_rows is still a matrix, so we can index it as such.
# Just like we can slice vectors, we can slice matrix rows or columns.
# In the below statement, we print all of the columns in the first 10 rows of wine_rows.
print(wine_rows[0:10,:])


# Assign all of the rows where the country equals "Turkey" to turkey_rows.
# Assign the first 10 rows where the year equals "1985" to rows_1985.
# Note that variable names in python can't start with numbers, so we can't start our name #with 1985.
turkey = world_alcohol[:,2] == "Turkey"
turkey_rows = world_alcohol[turkey,:]

year_1985 = world_alcohol[:,0] == "1985"
rows_1985 = world_alcohol[year_1985,:][0:10,:]
