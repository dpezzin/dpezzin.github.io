#!/usr/bin/env python
# Boolean vector corresponding to Canada and 1986.
canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == "1986")

# We can then use canada_1986 to subset a matrix -- it's just a normal boolean vector
print(world_alcohol[canada_1986,:])


# Assign all rows where the country is "Yemen" and the year is "1987" to yemen_1987.
# Assign all rows where the country is "Latvia", the year is "1989", and the type of alcohol is "Wine" to latvia_1989_wine.
yemen_1987_boolean = (world_alcohol[:,2] == "Yemen") & (world_alcohol[:,0] == "1987")
yemen_1987 = world_alcohol[yemen_1987_boolean,:]

latvia_1989_wine_boolean = (world_alcohol[:,2] == "Latvia") & (world_alcohol[:,0] == "1989") & (world_alcohol[:,3] == "Wine")
latvia_1989_wine = world_alcohol[latvia_1989_wine_boolean,:]