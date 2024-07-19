# New operators | and |= allow for merging and updating dictionaries.
# Introduced in Python 3.9 to make it easier to merge and update dictionaries.

# Merging Dictionaries with |
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)   # Output: {'a': 1, 'b': 3, 'c': 4}

# Updating Dictionaries with |=
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1 |= dict2

print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
# print(dict2)  # Output: {'b': 3, 'c': 4}

# Example 1: Simple merge
dict1 = {'x': 5, 'y': 6}
dict2 = {'y': 7, 'z': 8}
result = dict1 | dict2
print(result)  # Output: {'x': 5, 'y': 7, 'z': 8}

# Example 2: Updating in place
dict1 = {'x': 5, 'y': 6}
dict2 = {'y': 7, 'z': 8}
dict1 |= dict2
print(dict1)  # Output: {'x': 5, 'y': 7, 'z': 8}