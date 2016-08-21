#!/usr/bin/env python
# pass is a special keyword that tells Python to do nothing and keep going.
# We can't have zero lines inside the body of any statement ending with a colon 
#(for loop, function definition, if statement, and so on). Comments don't count as lines for this purpose.
invalid_int = ""
try:
    # This parsing will fail
    invalid_int = int(invalid_int)
except Exception:
    # Nothing will happen in the body of the except statement, because we are passing.
    pass

# invalid_int still has the same value.
print(invalid_int)

# We can also use the pass statement with for loops.
# (although it's less useful in this example)
a = [1,4,5]
for i in a:
    pass

# And if statements.
if 10 > 5:
    pass

# We can use the pass keyword inside the body of any statement that ends with a colon.
valid_int = "10"


# Use a try/except block to parse valid_int into an integer.
# Use the pass keyword inside the except block.
try:
    valid_int = int(valid_int)
except Exception:
    pass

