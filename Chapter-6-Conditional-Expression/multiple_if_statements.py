a = int(input("Enter your age: "))

# if statement no. 1:
if(a % 2 == 0):
    print("a is even")

# if statement no. 2:
if(a >= 18):
    print("You are above the age of consent")
    print("Good for you!")

elif(a < 0):
    print("You are entering an invalid negative age")
    print("Next time, please enter correct age!")

elif(a == 0):
    print("You are entering 0 which is not a valid age")
    print("Next time, please enter correct age!")    

else:
    print("You are below the age of consent")
    print("You are not allowed!")

print("End of Program !")