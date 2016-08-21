#!/usr/bin/env python


# Now that we recalculated the centroids, 
# let's re-run Step 1 (assign_to_cluster) and see how the clusters shifted.
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)


# Now we need to recalculate the centroids, and shift the clusters again.
centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)