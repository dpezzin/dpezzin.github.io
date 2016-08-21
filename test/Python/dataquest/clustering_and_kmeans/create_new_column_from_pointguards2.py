#!/usr/bin/env python


# First, drop the players who have 0 turnovers. 
# Not only did these players only play a few games, 
# making it hard to understand their true abilities, 
# but we also cannot divide by 0 when we calculate atr. 
point_guards = point_guards[point_guards['tov'] != 0]


# Utilize the same division technique we used with Points Per Game 
# to create the Assist Turnover Ratio (ast) column for point_guards.
point_guards['atr'] = point_guards['ast'] / point_guards['tov']
print(point_guards['atr'])
