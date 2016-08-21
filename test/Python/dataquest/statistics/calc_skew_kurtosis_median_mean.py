#!/usr/bin/env python
# The cleaned up data has been loaded into the titanic_survival variable


# Assign the mean of the "age" column of titanic_survival to mean_age.
# Assign the median of the "age" column of titanic_survival to median_age.
# Assign the skew of the "age" column of titanic_survival to skew_age.
# Assign the kurtosis of the "age" column of titanic_survival to kurtosis_age.
import numpy
from scipy.stats import skew
from scipy.stats import kurtosis
mean_age = titanic_survival["age"].mean()
median_age = numpy.median(titanic_survival["age"])
skew_age = skew(titanic_survival["age"])
kurtosis_age = kurtosis(titanic_survival["age"])