class Employee:
    language = "Python"     # This is a Class Attribute
    salary = 1200000

    # dunder method which is automatically called
    def __init__(self):     # constructor
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    # @staticmethod
    # def greet():    # decorator to mark greet as a static method 
    #     print("Good Moring!")   

akash = Employee()
akash.name = "Akash"
# akash.getInfo()         # Equivalent to Employee.getInfo(akash)
# Employee.getInfo(akash)   

# akash.greet()
print(akash.name, akash.salary)

darshit = Employee()
manab = Employee()