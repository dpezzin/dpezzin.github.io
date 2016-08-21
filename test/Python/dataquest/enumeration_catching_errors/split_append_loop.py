#!/usr/bin/env python
birth_years = []


# Loop through the rows in legislators
# Inside the loop, get the birthday column from the row, and split the birthday.
# After splitting the birthday, get the birth year, and append it to birth_years
# At the end, birth_years will contain the birth years of all the Congresspeople in the data.
for row in legislators:
    split_birthday = row[2].split("-")
    birth_year = split_birthday[0]
    birth_years.append(birth_year)