#!/usr/bin/env python


# prglngth_firsts_pmf and prglngth_others_pmf are both dictionaries 
# containing the probabilities of each value in their respective dataset 
# and column pairs occuring. prglngth_firsts_pmf contains probabilities 
# for prglngth in the firsts dataset.

# Plot both pmfs as basic bar charts, using the template plt.bar(x, y). 
# Be sure to use plt.show() after plotting each pmf. Also be sure to sort 
# the dictionary keys from lowest to highest before you plot.
prglngth_others_pmf = Pmf(others["prglngth"]).counts

import matplotlib.pyplot as plt

def get_plot_data(pmf):
    keys = sorted(pmf.keys())
    y = [pmf[k] for k in keys]
    return keys, y

firsts_pmf = get_plot_data(prglngth_firsts_pmf)
others_pmf = get_plot_data(prglngth_others_pmf)

plt.bar(firsts_pmf[0], firsts_pmf[1])
plt.show()

plt.bar(others_pmf[0], others_pmf[1])
plt.show()