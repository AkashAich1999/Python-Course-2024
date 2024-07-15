class Employee:
    language = "Python"         # This is a Class Attribute
    salary = 1200000

akash = Employee()
akash.language = "JavaScript"   # Changing Class Attribute
print(akash.language, akash.salary)    

# Note: Instance attributes, take preference over class attributes during assignment & retrieval.

# When looking up for harry.attribute it checks for the following: 
# 1) Is attribute present in object? 
# 2) Is attribute present in class? 