#!/usr/bin/env python
class Zoo():
    def __init__(self):
        self.animals = []

    # This is an instance method.
    # It can be invoked on any instance of this class.
    # Note that because it is an instance method, we still need to put in the self argument.
    def add_animal(self, animal):
        # This will add the animal to the list of animals that the instance is storing.
        self.animals.append(animal)

# We start with no animals.
san_diego_zoo = Zoo()
print(san_diego_zoo.animals)

# Then we get a panda!
san_diego_zoo.add_animal("panda")
print(san_diego_zoo.animals)

# The we get an orca!
san_diego_zoo.add_animal("orca")
print(san_diego_zoo.animals)


# Add a method called count_total_wins to the Team class.
# The method should take no arguments (except self), and should return the number of games the team won from 2009-2013.
# Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
# Use the instance method to assign the number of wins by the "Kansas City Chiefs" to chiefs_wins.
# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

class Team():
    def __init__(self, name):
        self.name = name

    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:
                count = count + 1
        return count

broncos = Team("Denver Broncos")
broncos_wins = broncos.count_total_wins()

chiefs = Team("Kansas City Chiefs")
chiefs_wins = chiefs.count_total_wins()
