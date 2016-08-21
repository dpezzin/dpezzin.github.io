#!/usr/bin/env python
# Enter code here.


# Create a new pandas data frame which contains just the point guards from the data set. 
# Point guards are specified as PG in the position column. 
# Assign the filtered data frame to point_guards.

point_guards = nba[nba['pos'] == 'PG']