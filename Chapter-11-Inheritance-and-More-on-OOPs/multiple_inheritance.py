class Employee:              # Base Class or Parent Class
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"Name of the Employee is: {self.name} and company is: {self.company}\n")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"His Favourite Language is: {self.language}\n")        

class Programmer(Employee, Coder):  # Derived Class or Child Class (Multiple Inheritance)
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"Company Name is: {self.company} and Employee Name is: {self.name} and He is Good with: {self.language} Language.\n")

e = Employee()
c = Coder()
p = Programmer()

e.show()

c.printLanguages()

p.show()
p.printLanguages()
p.showLanguage()