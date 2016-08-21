#!/usr/bin/env python
names = ["Jim", "Bob", "Bob", "JimBob", "Joe", "Jim"]
name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] = name_counts[name] + 1
    else:
        name_counts[name] = 1

		
		
# Count up how many times each female name occurs in legislators. First name is the second column.
# You'll need to make sure that gender (fourth column) equals "F", and that birth year (eighth column) is greater than 1940.
# Store the first name key and the counts in the female_name_counts dictionary.
# You'll need to use nested if statements to first check if gender and birth year are valid, and then to check if the first name is in female_name_counts.
# female_name_counts = {}
for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        if row[1] in female_name_counts:
            female_name_counts[row[1]] = female_name_counts[row[1]] + 1
        else:
            female_name_counts[row[1]] = 1