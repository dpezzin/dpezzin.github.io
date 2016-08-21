#!/usr/bin/env python
class Car():
    # The special __init__ function is run whenever a class is instantiated.
    # The init function can take arguments, but self is always the first one.
    # Self is a reference to the instance of the class.
    def __init__(self, car):
        # Using self before car means that car is an instance property.
        self.car = car

# When we instantiate the class, we pass in any arguments that the __init__ function needs.
# We skip the self argument.
accord = Car("Honda Accord")

# We set self.car in the __init__ function, but can print accord.car here.
# self is a reference to the instance of the class.
# It lets us interact with the class instance within the class.
print(accord.car)

# Instance properties are only available to instances, not to the classes.
# We couldn't print Car.car, for example.

class Team():
    name = "Tampa Bay Buccaneers"

	
# Modify the Team class so that name is an instance property.
# Make an instance of the class, passing in the value "Tampa Bay Buccaneers" to the __init__ function.
# Assign the instance to the variable bucs.
class Team():
    def __init__(self, name):
        self.name = name

bucs = Team("Tampa Bay Buccaneers")