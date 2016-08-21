#!/usr/bin/env python
def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        # Finish the logic
     return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)


# Finish the function, recalculate_centroids, that takes in the point_guards data frame object, 
# uses each cluster_id(from 0 to num_clusters - 1) to pull out all of the players in each cluster, 
# calculates the new geometric mean, and adds the cluster_id and the new geometric mean to 
# new_centroids_dict, the final dictionary to be returned.
def recalculate_centroids(df):
    new_centroids_dict = dict()
    
    for cluster_id in range(0, num_clusters):
        values_in_cluster = df[df['cluster'] == cluster_id]
        # Calculate new centroid using mean of values in the cluster
        new_centroid = [np.average(values_in_cluster['ppg']), np.average(values_in_cluster['atr'])]
        new_centroids_dict[cluster_id] = new_centroid
    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)