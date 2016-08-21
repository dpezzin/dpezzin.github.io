#!/usr/bin/env python
# The nfl data is loaded into the nfl variable.

# Loop through the nfl data.
# Count up how many games the "New England Patriots" won from 2009-2013.
# Assign the count to patriots_wins. The count should be an integer.
patriots_wins = 0
for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins += 1