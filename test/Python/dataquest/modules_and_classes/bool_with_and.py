#!/usr/bin/env python
its_raining = "Yes"
its_snowing = "No"

# Each statement is evaluated separately.
# If either of them is False on its own, then the whole statement is False.
print(its_raining == "Yes" and its_snowing == "Yes")

# If both evaluate to True, then the whole statement is True.
print(its_raining == "Yes" and its_snowing == "No")


# Assign a boolean that uses the and keyword and evaluates to True to a.
# Assign a boolean that uses the and keyword and evaluates to False to b.
a = its_raining == "Yes" and its_snowing == "No"
b = its_raining == "Yes" and its_snowing == "Yes"