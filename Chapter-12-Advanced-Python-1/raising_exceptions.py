a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if(b == 0):
    raise ZeroDivisionError("Cannot Divide Numerator with 0")

else:
    print(f"The Divison a/b is {a/b}")