#!/usr/bin/env python


# To generate the cluster_ids, let's iterate through each centroid and assign an integer 
# from 0 to k-1. For example, the first centroid will have a cluster_id of 0, while the 
# second one will have a cluster_id of 1. We'll write a function, centroids_to_dict, that 
# takes in the centroids data frame object, creates a cluster_id and converts the ppg and 
# atr values for that centroid into a list of coordinates, 
# and adds both the cluster_id and coordinates_list into the dictionary that's returned.

def centroids_to_dict(centroids):
    dictionary = dict()
    # iterating counter we use to generate a cluster_id
    counter = 0

    # iterate a pandas data frame row-wise using .iterrows()
    for index, row in centroids.iterrows():
        coordinates = [row['ppg'], row['atr']]
        dictionary[counter] = coordinates
        counter += 1

    return dictionary

centroids_dict = centroids_to_dict(centroids)