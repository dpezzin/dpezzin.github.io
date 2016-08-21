#!/usr/bin/env python
# Let's make a histogram class that counts up all the unique values in a column.
from collections import Counter
class Hist(object):
    def __init__(self, column):
        counts = Counter(column)
        self.counts = dict(counts)

# We can use the class to count up the unique values in prglngth.
prglngth_firsts_hist = Hist(firsts["prglngth"])
print(prglngth_firsts_hist.counts)

class Pmf(Hist):
    pass

	
# Extend the Pmf class to generate probabilities instead of counts. 
# Once easy way to achieve this is to divide the count of each unique 
# item by the total number of items. All the probabilities should sum to 1.

# Assign the dictionary containing the probability of each unique value 
# occuring in the column prglngth in firsts to prglngth_firsts_pmf.
class Pmf(Hist):
    def __init__(self, column):
        counts = Counter(column)
        self.counts = dict(counts)
        total = len(column)
        for c in self.counts:
            self.counts[c] /= total

prglngth_firsts_pmf = Pmf(firsts["prglngth"]).counts