a = 90

def fun():
    a = 3
    print(a, end=" ")   # 3

print(a, end=" ")       # 90
fun()
print(a)       # 90

# Output: 90 3 90

b = 45

def gfun():
    global b            # global keyword
    b = 3
    print(b, end=" ")   # 3

print(b, end=" ")       # 45
gfun()    
print(b, end=" ")       # 3

# Output: 45 3 3