#!/usr/bin/env python
import pandas as pd
from sklearn.cluster import KMeans


# While two clusters is interesting, it didn't tell us anything we don't already know.
# More clusters could show wings of each party, or cross-party groups.
# Let's try using 5 clusters to see what happens.
kmeans_model = KMeans(n_clusters=5, random_state=1).fit(votes.iloc[:, 3:])
labels = kmeans_model.labels_
# The republicans are still pretty solid, but it looks like there are two democratic "factions"
print(pd.crosstab(labels, votes["party"]))