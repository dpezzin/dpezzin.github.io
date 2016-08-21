#!/usr/bin/env python


# We can now find out which senators are in the "wrong" cluster.
# These senators are in the cluster associated with the opposite party.
# Let's call these types of voters "oddballs" (why not?)
# There aren't any republican oddballs
democratic_oddballs = votes[(votes["label"] == 1) & (votes["party"] == "D")]
# It looks like Reid has abstained a lot, which changed his cluster.
# Manchin seems like a genuine oddball voter.
print(democratic_oddballs["name"])