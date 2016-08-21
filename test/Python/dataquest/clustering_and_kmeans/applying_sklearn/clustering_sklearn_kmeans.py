#!/usr/bin/env python


# k-means clustering will try to make clusters out of the senators.
# Each cluster will contain senators whose votes are as similar to each other as possible.
# We'll need to specify the number of clusters we want upfront.
# Let's try 2 to see how that looks.

import pandas as pd

# The kmeans algorithm is implemented in the scikits-learn library
from sklearn.cluster import KMeans

# Create a kmeans model on our data, using 2 clusters.  random_state helps 
# ensure that the algorithm returns the same results each time.
kmeans_model = KMeans(n_clusters=2, random_state=1).fit(votes.iloc[:, 3:])

# These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
labels = kmeans_model.labels_

# The clustering looks pretty good!
# It's separated everyone into parties just based on voting history
print(pd.crosstab(labels, votes["party"]))