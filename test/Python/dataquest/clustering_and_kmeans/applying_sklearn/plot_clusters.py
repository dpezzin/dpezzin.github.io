#!/usr/bin/env python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# Let's explore our clusters a little more by plotting them out.
# Each column of data is a dimension on a plot, and we can't visualize 15 dimensions.
# We'll use principal component analysis to compress the vote columns into two.
# Then, we can plot out all of our senators according to their votes, and shade them by their cluster.
pca_2 = PCA(2)
# Turn the vote data into two columns with PCA
plot_columns = pca_2.fit_transform(votes.iloc[:,3:18])
# Plot senators based on the two dimensions, and shade by cluster label
# You can see the plot by clicking "plots" to the bottom right
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=votes["label"])
plt.show()