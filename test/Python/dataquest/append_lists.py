#!/usr/bin/env python
# The append method adds items to the end of lists.
# a will go from having no items in it to having 10 at index 0.
a = []
print(a)
a.append(10)
print(a)

# b will go from having one item to having two items.
b = [30]
print(b)
b.append(50)
print(b)

# We can setup an old list with items, and an empty new list.
old_list = [1,2,5,10]
new_list = []

# At the end of this loop, new_list will be equal to old_list.
# The loop will have gone through each item in old_list, starting from index 0, and appended it to the end of new_list.
for item in old_list:
    new_list.append(item)
print(new_list)

# append 60 to c. Then append 70 to c. c should end up with 4 items.
c = [20,30]
c.append(60)
c.append(70)