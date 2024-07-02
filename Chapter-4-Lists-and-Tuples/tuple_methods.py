friends = (1, 111, 11111, "Apple", "Orange", 57, 7.73, 57, False, "Akash", "Aich")
print(friends)

no = friends.count(77)
print(no)

no = friends.count(57)
print(no)

# i = friends.index(2)
# print(i)

i = friends.index(57)
print(i)

t1 = (1, 2, 3)
t2 = (4, 5, 6, 7)
concat = t1 + t2
print(concat)

t = (1, 2, 3)
repeated_t = t * 3
print(repeated_t)

tuple = (1, 2, 3)
print(2 in tuple)   # Output: True
print(4 in tuple)   # Output: False

print(len(tuple))   # 3

# Slicing
tuple = (1, 2, 3, 4, 5)
sliced = tuple[1:4]
print(sliced)       # Output: (2, 3, 4)

# Unpacking
tuple = (1, 2, 3)
a, b, c = tuple
print(a, b, c)      # Output: 1 2 3