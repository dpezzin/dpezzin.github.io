#!/usr/bin/env python
# Luckily, pandas dataframes have a method that can drop rows that have missing data
# Let's look at how big the dataframe is first
print(titanic_survival.shape)

# There were 1310 passengers on the titanic, according to our data
# Now let's drop any row with missing data
# The dropna method on dataframes will do this for us
# Any row with any missing values will be removed
new_titanic_survival = titanic_survival.dropna()

# Hmm, it looks like we were too zealous with dropping rows with na values
# We now have no rows in our dataframe
# This is because some of the later columns, which aren't immediately relevant to our analysis, have a lot of missing values
print(new_titanic_survival.shape)

# We can use the subset keyword argument to the dropna method to only drop rows if there are na values in certain columns
# This will drop any row where the embarkation port (where people boarded the Titanic), or cabin number is missing
new_titanic_survival = titanic_survival.dropna(subset=["embarked", "cabin"])

# This is much better -- we have removed only the rows that we need to remove.
print(new_titanic_survival.shape)


# Remove the NaN values in the "age" and "sex" columns.
# Assign the result to new_titanic_survival.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])