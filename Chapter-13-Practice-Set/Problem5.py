# 5. Write a program to find the maximum of the numbers in a list using the reduce function. 

from functools import reduce
l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

def greater(a, b):
    if(a > b):
        return a
    return b

print(reduce(greater, l))