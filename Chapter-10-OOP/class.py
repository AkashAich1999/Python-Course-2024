class Employee:
    language = "Py"     # This is a Class Attribute
    salary = 1200000

akash = Employee()
akash.name = "Akash"    # This is an Instance Attribute
print(akash.name, akash.language, akash.salary)

darshit = Employee()
darshit.name = "Darshit"
print(darshit.name, darshit.language, darshit.salary)