# 2. Write a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.
 
sub1 = int(input("Enter Subject 1 Marks: "))
sub2 = int(input("Enter Subject 2 Marks: "))
sub3 = int(input("Enter Subject 3 Marks: "))
p = (sub1 + sub2 + sub3)/3 

if(sub1 < 33 or sub2 < 33 or sub3 < 33 or p < 40):
    print("Failed")

else:
    print("Passed")     