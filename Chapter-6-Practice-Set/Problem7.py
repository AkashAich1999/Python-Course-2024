# 7. Write a program to find out whether a given post is talking about “Akash” or not.

post = input("Enter the Post: ")

if("Akash".lower() in post.lower()):
    print("This Post is Talking about Akash")

else:
    print("This Post is Not Talking about Akash")    