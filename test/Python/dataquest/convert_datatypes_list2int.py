#!/usr/bin/env python
# Now that we know about the int() function, let's use it to convert the values in a list to integers.
the_list = ['1', '2', '3']
new_list = []

# Loop through the_list
for item in the_list:
    # Get the int value of the item in the list
    item_int = int(item)
    # Add the int item to the new list
    new_list.append(item_int)
# Print out the new list
print(new_list)

a = ['10', '15', '20', '35']
new_a = []

# Convert all the values in a into integers using a for loop. append them to new_a.
for item in a:
    item_int = int(item)
    new_a.append(item_int)
