#!/usr/bin/env python
from sklearn.cluster import KMeans


# As you repeat Steps 1 and 2 and run visualize_clusters, 
# you'll notice that a few of the points are changing clusters 
# between every iteration (especially in areas where 2 clusters almost overlap), 
# but otherwise, the clusters visually look like they don't move a lot after every iteration. 

# This means 2 things:

# K-Means doesn't cause massive changes in the makeup of clusters between iterations, 
# meaning that it will always converge and become stable

# Because K-Means is conservative between iterations, where we pick 
# the initial centroids and how we assign the players to clusters initially matters a lot
# To counteract these problems, the sklearn implementation of K-Means does some intelligent things 
# like re-running the entire clustering process lots of times with random initial centroids 
# so the final results are a little less biased on one passthrough's initial centroids.
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters)