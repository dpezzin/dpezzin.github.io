#!/usr/bin/env python
dogs = ["labrador", "poodle", "collie"]
cats = ["siamese", "persian", "somali"]

# Enumerate the dogs list, and print the values.
for i, dog in enumerate(dogs):
    # Will print the dog at the current loop iteration.
    print(dog)
    # This will equal dog.  Prints the dog at index i.
    print(dogs[i])
    # Print the cat at index i.
    print(cats[i])

	
# Use a for loop to enumerate the ships list.
# In the body of the loop, print the ship at the current index, then the car at the current index.
# Make sure you have two separate print statements.
ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])