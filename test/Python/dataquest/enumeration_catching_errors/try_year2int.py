#!/usr/bin/env python
# The legislators variable has been loaded.


# Loop over the rows in legislators, and convert the values in the birth year column to integers.
# In cases where parsing fails, assign 0 as the value.
for row in legislators:
    try:
        row[7] = int(row[7])
    except Exception:
        row[7] = 0