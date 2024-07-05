 # 6. Write a program to calculate the factorial of a given number using while loop. 

n = int(input("Enter Number:"))

fact = 1
i = 1

while(i <= n):
    fact *= i
    i += 1

print(fact)    