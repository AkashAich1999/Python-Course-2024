# Without using Enumerate:

# l = [1, 22, 333, 444, 55555]

# index = 0
# for item in l:
#     print(f"Item Number is {item} at index {index}")
#     index += 1

# Using Enumerate:
l = [1, 22, 333, 444, 55555]

for index, item in enumerate(l):
    print(f"Item Number is {item} at index {index}") 