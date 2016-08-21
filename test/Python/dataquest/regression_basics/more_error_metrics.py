#!/usr/bin/env python
# The test set predictions are in the predictions variable.
# MSE and RMSE, because they square the errors, penalize large errors way out of proportion to small errors. 
# MAE, on the other hand, doesn't. MAE can be useful, because it is a more accurate look at the average error.
import math


# Calculate the RMSE between the test set predictions and the actual values. Assign the result to rmse.
# Calculate the MAE between the test set predictions and the actual values. Assign the result to mae.

rmse = math.sqrt(sum((predictions - test["next_day"]) ** 2) / len(predictions))
mae = sum(abs(predictions - test["next_day"])) / len(predictions)