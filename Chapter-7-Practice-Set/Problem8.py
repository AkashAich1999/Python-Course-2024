# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 

n = int(input("Enter n: "))

for i in range(0,n): 
    print("*" * (i+1))