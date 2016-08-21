#!/usr/bin/env python
# Let's say that these lists are both columns in a matrix.  Index 0 in both is the first row, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]


# Compute the average savings for everyone who is "male". Assign the result to male_savings.
# Compute the average savings for everyone who is "female". Assign the result to female_savings.
male_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
female_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list)