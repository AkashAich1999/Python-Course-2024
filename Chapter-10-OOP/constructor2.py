class Employee:
    language = "Python"     # This is a Class Attribute
    salary = 1200000

    # dunder method which is automatically called
    def __init__(self, name, salary, language):     # constructor
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an Object.")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

akash = Employee("Akash Aich", 1300000, "JavaScript")
print(akash.name, akash.salary)