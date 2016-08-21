#!/usr/bin/env python
# The actual values are in to_predict, and the predictions are in next_day_predictions.


# Compute the mean square error of our predictions. Assign the result to mse.
mse = sum((to_predict - next_day_predictions) ** 2)
mse /= len(next_day_predictions)