# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language.")

# a = Employee()
# b = Programmer()

# print(a.company, b.company)

class Employee:              # Base Class or Parent Class
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):  # Derived Class or Child Class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language.")

a = Employee()
b = Programmer()

print(a.company, b.company)