#!/usr/bin/env python
import matplotlib.pyplot as plt


# Make a scatterplot for the test dataframe with value on the x axis, and next_day on the y axis. 
# Draw a line over this that has value on the x axis, and the predictions on the y axis. 
# The predictions are in the predictions variable.

# Make a scatterplot with the actual values in the training set
plt.scatter(train["value"], train["next_day"])
plt.plot(train["value"], regressor.predict(train[["value"]]))
plt.show()

plt.scatter(test["value"], test["next_day"])
plt.plot(test["value"], predictions)
plt.show()