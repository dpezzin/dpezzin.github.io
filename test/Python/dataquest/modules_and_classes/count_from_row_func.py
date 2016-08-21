#!/usr/bin/env python
# The nfl data is loaded into the nfl variable.

# Make a function that will take a team name, in the form of a string, as input.
# The function should output the number of wins the team had from 2009-2013, as an integer.
# Use the function to assign the number of wins by the "Dallas Cowboys" to cowboys_wins.
# Use the function to assign the number of wins by the "Atlanta Falcons" to falcons_wins.
def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count = count + 1
    return count

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")

print(cowboys_wins)
print(falcons_wins)