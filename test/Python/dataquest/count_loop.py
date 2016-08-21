#!/usr/bin/env python
# In order to make it easier to use the weather column that we just parsed, we're going to automatically include it from now on.
# It's been specially added before our code runs.
# We can interact with it normally -- it's a list.
print(weather[0])

count = 0

for item in weather:
    count = count + 1