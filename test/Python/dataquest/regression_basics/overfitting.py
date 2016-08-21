#!/usr/bin/env python
import numpy as np
import random

# Set a random seed to make the shuffle deterministic.
np.random.seed(1)
random.seed(1)
# Randomly shuffle the rows in our dataframe
sp500 = sp500.loc[np.random.permutation(sp500.index)]

# Select 70% of the dataset to be training data
highest_train_row = int(sp500.shape[0] * .7)
train = sp500.loc[:highest_train_row,:]

# Select 30% of the dataset to be test data.
test = sp500.loc[highest_train_row:,:]

regressor = LinearRegression()


# Train regressor using the value column in train. Make predictions on the test set. Calculate the MSE in the test set, and assign the result to mse.
regressor.fit(train[["value"]], train["next_day"])
predictions = regressor.predict(test[["value"]])
mse = sum((predictions - test["next_day"]) ** 2) / len(predictions)