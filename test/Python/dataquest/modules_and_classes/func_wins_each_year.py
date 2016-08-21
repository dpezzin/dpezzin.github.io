#!/usr/bin/env python
# We'll need to create a new function to returns wins for each year.
# It will call nfl_wins_by_year as part of its computations.
def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

def nfl_wins_by_year(team):
    win_dict = {}
    # Fill in code here to compute the wins for each year and store them in win_dict
    return win_dict
	
	
# Make a new function that calls on the nfl_wins_by_year function to compute wins for each year from 2009 - 2013.
# Valid years are "2009", "2010", "2011", "2012", and "2013".
# The function should return a dictionary with the years as keys, and the number of wins in each year as values.
# Use the function to assign the number of wins by year by the "Miami Dolphins" to dolphins_wins_by_year.
# Use the function to assign the number of wins by year by the "San Diego Chargers" to chargers_wins_by_year.
def nfl_wins_by_year(team):
    win_dict = {}
    for year in ["2009", "2010", "2011", "2012", "2013"]:
        win_dict[year] = nfl_wins_in_a_year(team, year)
    return win_dict

dolphins_wins_by_year = nfl_wins_by_year("Miami Dolphins")
chargers_wins_by_year = nfl_wins_by_year("San Diego Chargers")