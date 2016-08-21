#!/usr/bin/env python
# We can check if a key is in a dictionary with the in statement.
the_dict = {"robin": "red", "cardinal": "red", "oriole": "orange", "lark": "blue"}

# This is True
print("robin" in the_dict)

# This is False
print("crow" in the_dict)

# We can also assign the boolean to a variable
a = "cardinal" in the_dict
print(a)


# Check whether "jupiter" is in dict2 and assign the result to b. 
# Check whether "earth" is in dict2 and assign the result to c.
dict2 = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

b = "jupiter" in dict2
c = "earth" in dict2