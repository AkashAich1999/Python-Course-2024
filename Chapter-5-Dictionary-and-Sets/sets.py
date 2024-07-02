s = {1, 5, 32}
print(s)

# Empty Set
e = set()   # Don't use s = {} as it will Create an Empty Dictionary.
print(e)
e.add(7)
print(e)

s = {1, 5, 32, 5, 5, 5}
print(s)    # {32, 1, 5}  Unique (Elements do not Repeat) & Ordered is Not Maintained.
# If maintaining order is important than we have to use List.

