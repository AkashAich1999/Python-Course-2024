# String is a data type in python. 
# String is a sequence of characters enclosed in quotes.

a = 'Akash'     # Single Quoted String
b = "Akash"     # Double Quoted String
c = '''Akash''' # Triple Quoted String

# String is Immutable in Python. That means it cannot be Changed after it got Created.

# name  =  "A  k  a  s  h"   ==> Length = 5
#           0  1  2  3  4
#          -5 -4 -3 -2 -1

# String Slicing
name = "Akash"
# print(len(name))    # 5
nameshort = name[0:3]   # Start from index 0 all the way till 3 (Excluding 3)
print(nameshort)    # Aka
character1 = name[1]
print(character1)   # k