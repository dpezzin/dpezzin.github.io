#!/usr/bin/env python
# Classes are defined with the class keyword.
# Then a space, then the class name.
# The parentheses are used to denote which class this class inherits from.
# We'll get to inheritance later on -- it's a pretty deep topic.
class NFLTeam():
    # Classes can have class properties.
    # These properties can then be accessed later on.
    # Properties are just variables that are contained in a class.
    name = "Pittsburgh Steelers"

# After we define a class, we create an instance of it.
steelers = NFLTeam()

# We can access the class property.
print(steelers.name)

# The steelers variable is called an instance of the class.
# NFLTeam is the class.
# Because name is a class property, not an instance property, we can also access it directly.
print(NFLTeam.name)


# Make a class called Team.
# Give it a class property called name, with the value "Tampa Bay Buccaneers".
# Make an instance of the class, and assign it to the variable bucs.
class Team():
    name = "Tampa Bay Buccaneers"

bucs = Team()