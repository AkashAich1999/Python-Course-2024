s = {1, 5, 32, 5, 5, 5, "Akash"}
print(s, type(s))   # {32, 1, 5, 'Akash'} <class 'set'>
print(len(s))

# Method 1
s.add(777)
print(s, type(s))   # {32, 1, 5, 777, 'Akash'} <class 'set'>
print(len(s))

# Method 2
s.remove(5)
print(s, type(s))
print(len(s))

# Method 3
s.pop()
print(s, type(s))
print(len(s))

# Method 4
s.pop()
print(s, type(s))
print(len(s))

# Method 5
# s.clear()     # Empties the Set