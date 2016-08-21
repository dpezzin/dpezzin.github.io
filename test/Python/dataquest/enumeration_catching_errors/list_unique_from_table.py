#!/usr/bin/env python
# We can use the set() function to convert lists into sets.
# A set is a data type, just like a list, but it only contains each value once.
car_makers = ["Ford", "Volvo", "Audi", "Ford", "Volvo"]

# Volvo and ford are duplicates
print(car_makers)

# Converting to a set
unique_car_makers = set(car_makers)
print(unique_car_makers)

# We can't index sets, so we need to convert back into a list first.
unique_cars_list = list(unique_car_makers)
print(unique_cars_list[0])

genders_list = []
unique_genders = set()
unique_genders_list = []


# Loop through the rows in legislators, and extract the gender column (fourth column)
# Append the genders to genders_list.
# Then turn genders_list into a set, and assign it to unique_genders
# Finally, convert unique_genders back into a list, and assign it to unique_genders_list.
for row in legislators:
    genders_list.append(row[3])
unique_genders = set(genders_list)
unique_genders_list = list(unique_genders)
print(unique_genders_list[0])