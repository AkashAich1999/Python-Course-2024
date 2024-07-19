# Without Using List Comprehensions:
myList = [1, 7, 12, 11, 22]

squaredList = []
for item in myList:
    squaredList.append(item * item)

print(squaredList)

# With Using List Comprehensions:
nList = [1, 7, 12, 11, 22]
sqList = [i*i for i in nList]
print(sqList)

# Another Program:
list1 = [1, 7, 12, 11, 22]
list2 = [i*i for i in list1 if i > 8]
print(list2)