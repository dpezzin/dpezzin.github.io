#!/usr/bin/env python
# Let's say the US invades Canada (not that they should)
# This will replace all instances of "Canada" in the country column with "United States of America"
world_alcohol[:,2][world_alcohol[:,2] == "Canada"] = "United States of America"
print(world_alcohol[:,2][world_alcohol[:,2] == "Canada"])

# We don't have to subset before we replace
# Trinidad and Tobago can invade the whole world, and replace all countries
world_alcohol[:,2] = "Trinidad and Tobago"
print(world_alcohol[:,2][0:10])


# Replace all instances of '1986' in the year column (column 1) with '2014'.
# Replace all the values in the type column (column 4) with 'Grog' (pirates have taken over the world).
world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'
world_alcohol[:,3] = 'Grog'