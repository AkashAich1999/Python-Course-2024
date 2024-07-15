class Employee:
    language = "Python"     # This is a Class Attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

akash = Employee()
akash.getInfo()         # Employee.getInfo(akash)
Employee.getInfo(akash)    