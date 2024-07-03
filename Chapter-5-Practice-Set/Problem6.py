# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter Friends Name 1: ")
lang = input("Enter Favorite Language 1:")
d.update({name: lang})

name = input("Enter Friends Name 2: ")
lang = input("Enter Favorite Language 2:")
d.update({name: lang})

name = input("Enter Friends Name 3: ")
lang = input("Enter Favorite Language 3:")
d.update({name: lang})

name = input("Enter Friends Name 4: ")
lang = input("Enter Favorite Language 4:")
d.update({name: lang})

print(d)