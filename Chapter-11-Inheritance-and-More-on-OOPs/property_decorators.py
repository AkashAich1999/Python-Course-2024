# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is: {cls.a}")

#     @property
#     def name(self):
#         return self.ename
    
#     @name.setter
#     def name(self, value):
#         self.ename = value

# e = Employee()
# e.a = 45

# print(Employee.name)    # <property object at 0x0000018B7090DCB0>
# e.name = "Akash Aich"   
# print(e.name)           # Akash Aich
# print(Employee.name)    # <property object at 0x0000018B7090DCB0>

# e.show()

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

print(Employee.name)    # <property object at 0x0000018B7090DCB0>
e.name = "Akash Aich"   
print(e.name)           # Akash Aich
print(Employee.name)    # <property object at 0x0000018B7090DCB0>

e.show()