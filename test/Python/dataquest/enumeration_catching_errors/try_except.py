#!/usr/bin/env python
# Cannot be parsed into an int with the int() function.
invalid_int = ""

# Can be parsed into an int.
valid_int = "10"

# Parse the valid int
try:
    valid_int = int(valid_int)
except Exception:
    # This code is never run, because there is no error parsing valid_int into an integer.
    valid_int = 0

# Try to parse the invalid int
try:
    invalid_int = int(invalid_int)
except Exception:
    # The parsing fails, so we end up here.
    # The code here will be run, and will assign 0 to invalid_int.
    invalid_int = 0

print(valid_int)
print(invalid_int)

another_invalid_int = "Oregon"
another_valid_int = "1000"


# Use try/except statements to parse another_invalid_int and another_valid_int.
# Assign 0 to another_invalid_int in the except block.
# At the end, another_valid_int will be parsed properly, and another_invalid_int will be 0.
try:
    another_invalid_int = int(another_invalid_int)
except Exception:
    another_invalid_int = 0

try:
    another_valid_int = int(another_valid_int)
except Exception:
    another_valid_int = 0
