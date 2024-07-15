class Employee:
    language = "Python"     # This is a Class Attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():    # decorator to mark greet as a static method 
        print("Good Moring!")   

akash = Employee()
akash.getInfo()         # Equivalent to Employee.getInfo(akash)
Employee.getInfo(akash)   

akash.greet()