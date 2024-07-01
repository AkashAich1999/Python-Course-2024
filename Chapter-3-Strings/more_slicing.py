# Slicing with Skip Value

word = "amazing"
print(word[1 : 6 : 2])  # mzn

a = "0123456789"
print(a[1 : 7 : 3])   # 14
print(a[1 : 7 : 2])   # 135

b = "abcdefghijklmnopqrstuvwxyz"
print(b[1 : 9 : 3])  # beh
print(b[1 : 9 : 4])  # bf

# Other Advanced Slicing Techniques:

word = "amazing"
print(word[:7])     # amazing
print(word[0:])     # amazing