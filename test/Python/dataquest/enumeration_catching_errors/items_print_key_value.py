#!/usr/bin/env python
animal_types = {"robin": "bird", "pug": "dog", "osprey": "bird"}

# The .items method lets us access a dictionary key and value in a loop.
for key,value in animal_types.items():
    print(key)
    print(value)
    # This is equal to the value
    print(animal_types[key])

	
# Use the .items() method along with a for loop to loop through plant_types.
# Inside the loop, print the key, and then the value.
plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for k,v in plant_types.items():
    print(k)
    print(v)