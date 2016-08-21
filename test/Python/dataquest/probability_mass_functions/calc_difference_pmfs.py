#!/usr/bin/env python


# Make a list of all the keys that occur in prglngth_firsts_pmf and prglngth_others_pmf. 
# These keys should be unique (each value in the list should only occur once). 
# Sort this list in ascending order. Assign this to prglngth_all_keys.

# For each key in prglngth_all_keys, find the corresponding probability in prglngth_firsts_pmf 
#(probability is 0 if key not found) and subtract the corresponding probability in prglngth_others_pmf. 
# Make a list with all the results, called prglngth_prob_diffs.

# Make a basic bar plot with prglngth_all_keys on the x axis, and prglngth_prob_diffs on the y axis.

combined_keys = list(prglngth_firsts_pmf.keys()) + list(prglngth_others_pmf.keys())
unique_keys = list(set(combined_keys))
all_keys = sorted(unique_keys)
prglngth_prob_diffs = [prglngth_firsts_pmf.get(k, 0) - prglngth_others_pmf.get(k, 0) for k in all_keys]

plt.bar(all_keys, prglngth_prob_diffs)
plt.show()