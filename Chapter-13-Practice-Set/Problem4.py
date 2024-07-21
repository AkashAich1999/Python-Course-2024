# 4. Write a program to filter a list of numbers which are divisible by 5. 

def divisibleBy5(n):
    if(n % 5 == 0):
        return True
    return False

l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

f = filter(divisibleBy5, l)

print(list(f))