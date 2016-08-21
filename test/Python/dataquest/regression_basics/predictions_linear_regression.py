#!/usr/bin/env python

# Instead of using statsmodels like we did earlier, we can use the linear regression class in the sckit-learn package. 
# This is the standard package for machine learning in python, and it's going to be used extensively in future lessons.
# In order to use an algorithm in the scikit-learn package, we first have to initialize the algorithm class with some parameters. 
# We can then call the class to predict values.

# Import the linear regression class
from sklearn.linear_model import LinearRegression

# Initialize the linear regression class.
regressor = LinearRegression()

# We're using 'value' as a predictor, and making predictions for 'next_day'.
# The predictors need to be in a dataframe.
# We pass in a list when we select predictor columns from "sp500" to force pandas not to generate a series.
predictors = sp500[["value"]]
to_predict = sp500["next_day"]

# Train the linear regression model on our dataset.
regressor.fit(predictors, to_predict)

# Generate a list of predictions with our trained linear regression model
next_day_predictions = regressor.predict(predictors)
print(next_day_predictions)