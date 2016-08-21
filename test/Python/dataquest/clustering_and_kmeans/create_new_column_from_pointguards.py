#!/usr/bin/env python


# While our dataset doesn't come with Points Per Game values, 
# we can easily calculate those using each player's total points (pts) 
# and the number of games (g) they played. Let's take advantage of pandas' 
# ability to multiply and divide columns to create the Points Per Game ppg 
# column by dividing the pts and g columns.
point_guards['ppg'] = point_guards['pts'] / point_guards['g']

# Sanity check, make sure ppg = pts/g
point_guards[['pts', 'g', 'ppg']].head(5)

print(point_guards['ppg'])