# 1. Write a program using functions to find greatest of three numbers.  
 
def greatest(a, b, c):
    if(a == b and b == c):
        print("All the 3 Numbers are Same.")
    elif(a > b and a> c):
        print("a is Greatest.")
    elif(b > a and b > c):       
        print("b is Greatest.")
    elif(c > a and c > b):       
        print("c is Greatest.")    

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
greatest(a,b,c)