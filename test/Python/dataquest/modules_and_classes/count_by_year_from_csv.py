#!/usr/bin/env python
import csv
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

		
# Add a method to the Team class that computes wins by year for the team.
# The wins_by_year function should return a dictionary with each year from 
# 2009-2013 as keys, and the number of wins in that year as values.
# Valid years are "2009", "2010", "2011", "2012", and "2013".
# Use the instance method to assign the number of wins by year by the 
# "San Francisco 49ers" to niners_wins_by_year.
    def wins_by_year(self):
        years = ["2009", "2010", "2011", "2012", "2013"]
        wins = {}
        for year in years:
            count = 0
            for row in self.nfl:
                if row[2] == self.name and row[0] == year:
                    count += 1
            wins[year] = count
        return wins

niners = Team("San Francisco 49ers")
niners_wins_by_year = niners.wins_by_year()
