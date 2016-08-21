#!/usr/bin/env python
# Modify this function to also take a year as input, and returns the wins by the team in the year.
def nfl_wins(team):
    count = 0
    for row in nfl:
        # We need to ensure that we only increment the count when the row pertains to the year we want.
        if row[2] == team:
            count = count + 1
    return count

	
# Modify the nfl_wins function so it will take a team name, in the form of a string, and a year, in the form of an string, as input.
# The only valid years are "2009", "2010", "2011", "2012", and "2013".
# Remember that the years are stored as strings in the data, so we also have to use strings for consistency.
# The function should output the number of wins the team had in the given year, as an integer.
# Use the function to assign the number of wins by the "Cleveland Browns" in 2010 to browns_2010_wins.
# Use the function to assign the number of wins by the "Philadelphia Eagles" in 2011 to eagles_2011_wins.
def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

browns_2010_wins = nfl_wins_in_a_year("Cleveland Browns", "2010")
eagles_2011_wins = nfl_wins_in_a_year("Philadelphia Eagles", "2011")