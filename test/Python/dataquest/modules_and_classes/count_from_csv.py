#!/usr/bin/env python
import csv
class Team():
    def __init__(self, name):
        self.name = name

    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:
                count = count + 1
        return count

# Add in code to read the csv nfl data to the __init__ method.
# Store the nfl data in the self.nfl instance property.
# Then convert the count_total_wins function to use the self.nfl property.
# Use the instance method to assign the number of wins by 
# the "Jacksonville Jaguars" to jaguars_wins.
		
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars = Team("Jacksonville Jaguars")
jaguars_wins = jaguars.count_total_wins()
