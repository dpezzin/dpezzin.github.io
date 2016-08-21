#!/usr/bin/env python


# Use matplotlib to create a scatter plot with Points Per Game (ppg) 
# on the X axis and Assist Turnover Ratio (atr) on the Y axis.
plt.scatter(point_guards['ppg'], point_guards['atr'], c='y')
plt.title("Point Guards")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
