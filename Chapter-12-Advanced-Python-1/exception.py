# try:
#     a = int(input("Hey, Enter a Number: "))
#     print(a)

# except Exception as e:      # This will Prevent Application Crashing
#     print(e)

# print("Thank You!")  

try:
    a = int(input("Hey, Enter a Number: "))
    print(a)

except ValueError as v:
    print("Hey!")
    print(v)

except ZeroDivisionError as z:
    print("Hi!")
    print(z)

except TypeError as t:
    print("Hello!")
    print(t)    

except Exception as e:
    print(e)    

print("Thank You!")    