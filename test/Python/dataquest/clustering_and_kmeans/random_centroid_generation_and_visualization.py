#!/usr/bin/env python


# To start, select 5 players at random 
# and assign their coordinates as the initial centroids of the just created clusters.
num_clusters = 5

# Use numpy's random function to generate a list, length: num_clusters, of indices
random_initial_points = np.random.choice(point_guards.index, size=num_clusters)


# Step 1 (Assign Points to Clusters) For each player, calculate the Euclidean distance between 
# that player's coordinates, or values for atr & ppg, and each of the centroids' coordinates. 
# Assign the player to the cluster whose centroid is the closest to, 
# or has the lowest Euclidean distance to, the player's values.

# Step 2 (Update New Centroids of the Clusters) For each cluster, compute the new centroid by 
# calculating the geometric mean of all of the points (players) in that cluster. We calculate 
# the geometric mean by taking the average of all of the X values (atr) 
# and the average of all of the Y values (ppg) of the points in that cluster.

# Iterate Repeat steps 1 & 2 until the clusters are no longer moving and have converged.

# Use the random indices to create the centroids
centroids = point_guards.ix[random_initial_points]


# Let's plot the centroids, in addition to the point_guards, so we can see where the randomly 
# chosen centroids started out.
plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow')
plt.scatter(centroids['ppg'], centroids['atr'], c='red')
plt.title("Centroids")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)