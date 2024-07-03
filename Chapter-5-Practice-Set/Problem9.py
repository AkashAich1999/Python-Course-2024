# 9. Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}

# No, We cannot change the values inside a list which is contained in a set. 
# This is because lists are mutable and sets require all their elements to be immutable (hashable). 
# If we try to include a list in a set, Python will raise a TypeError.

# To achieve a similar result, we can use a tuple instead of a list since tuples are immutable:

# python Code
# s = {8, 7, 12, "Harry", (1, 2)}
# This will work without raising an error.
