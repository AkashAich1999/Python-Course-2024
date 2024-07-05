# 5. Write a program to find the sum of first n natural numbers using for loop. 

n = int(input("Enter Number: "))

i = 1
sum = 0

for i in range(0, n+1):
    sum += i
    
print(sum)