# 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter Username: ")

if(len(username) < 10):
    print("Your username contains less than 10 Characters !")

else:
    print("Your username contains more than or equal to 10 Characters !")