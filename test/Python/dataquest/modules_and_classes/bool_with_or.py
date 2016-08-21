#!/usr/bin/env python
current_president = "Barack Obama"

# Each statement is evaluated separately.
# If either of them is True on its own, then the statement is True.
print(current_president == "Barack Obama" or current_president == "George Bush")

# If all of the statements evaluate to False, then the statement is False.
print(current_president == "Eminem" or current_president == "Kanye West")


# Assign a boolean that uses the or keyword and evaluates to True to a.
# Assign a boolean that uses the or keyword and evaluates to False to b.
a = current_president == "Barack Obama" or current_president == "George Bush"
b = current_president == "Eminem" or current_president == "Kanye West"